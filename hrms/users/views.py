from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, CompanyStatusSerializer
from company.models import CompanyDetails  
from rest_framework_simplejwt.tokens import AccessToken  
from datetime import timedelta

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)

            
            # Generate the access token
            access_token = str(refresh.access_token)
            # Generate the refresh token
            refresh_token = str(refresh)
            
            # Fetch the user's company details (ensure company is a ForeignKey in Login model)
            company = user.company if user.company else None

            # Decode the access token using SimpleJWT's AccessToken class for proper verification
            try:
                decoded_token = AccessToken(access_token)  # This automatically verifies the token's signature and expiration
                print("Decoded token:", decoded_token)
                print("Token expires at:", decoded_token['exp'])

            except TokenError as e:
                # Handle any errors that occur during token decoding
                return Response({"error": f"Token error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

            # Return the relevant fields to the frontend
            return Response({
                'access': access_token,  # Return access token to the frontend
                'refresh': refresh_token,
                'role': user.role,
                'user_id': user.id,
                'is_company_setup_complete': user.is_company_setup_complete,  # Ensure this is updated in DB
                'is_payroll_setup_complete': user.is_payroll_setup_complete,  # Fetch from CompanyDetails
                'company_id': company.companyId if company else None,  # Send company ID to the frontend
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class CompanyStatusView(APIView):
    def get(self, request, user_id):
        user = Login.objects.get(id=user_id)
        if user.company:  # Ensure user has an associated company
            company = user.company
            company_status = {
                'company_setup_done': company.isCompanyDetailsCompleted,  # Ensure field exists in CompanyDetails
                'payroll_setup_done': company.payroll_done,  # Ensure field exists in CompanyDetails
                'employee_setup_done': company.employee_setup_done,  # Ensure field exists in CompanyDetails
            }
            return Response(company_status, status=status.HTTP_200_OK)
        return Response({"error": "Company setup not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, user_id):
        user = Login.objects.get(id=user_id)  # Fetch the user

        company_id = request.data.get('company_id')
        if not company_id:
            return Response({"error": "Company ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Use companyId instead of id
            company = CompanyDetails.objects.get(companyId=company_id)  # Fetch the company by companyId
        except CompanyDetails.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

        # Link company to user
        user.company_id = company.companyId
        user.is_company_setup_complete = True  # Mark the company setup as complete
        user.role = "admin"
        user.is_admin = True
        user.save()

        return Response({"message": "Company setup updated successfully"}, status=status.HTTP_200_OK)



