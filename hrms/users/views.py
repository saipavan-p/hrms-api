# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Login
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserSerializer, LoginSerializer

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


#New roles
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Login
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import UserSerializer, LoginSerializer, CompanyStatusSerializer
# from company.models import CompanyDetails

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'is_admin': user.is_admin,
#                 'company_id': user.company.id if user.company else None,
#             })
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# class CompanyStatusView(APIView):
#     def get(self, request, user_id):
#         user = Login.objects.get(id=user_id)
#         if user.company:
#             company = user.company
#             company_status = {
#                 'company_setup_done': company.setup_done,
#                 'payroll_setup_done': company.payroll_done,
#                 'employee_setup_done': company.employee_setup_done,
#             }
#             return Response(company_status, status=status.HTTP_200_OK)
#         return Response({"error": "Company setup not found"}, status=status.HTTP_404_NOT_FOUND)


from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, CompanyStatusSerializer
from company.models import CompanyDetails  # Import CompanyDetails from the company app

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             refresh = RefreshToken.for_user(user)
            
#             # Check if the user has completed the company setup
#             if user.is_company_setup_complete:
#                 next_url = '/employeelist/'
#             else:
#                 next_url = '/companysetup/'
                
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'role': user.role,
#                 'next_url': next_url,
#                 'user_id': user.id
#             })
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            
            # Ensure you are fetching the correct company and payroll status from the database
            # company = user.company  # Assuming there's a company ForeignKey in Login model
            # Fetch the user's company details (ensure company is a ForeignKey in Login model)
            company = user.company if user.company else None

            # Return the relevant fields to the frontend
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'role': user.role,
                'user_id': user.id,
                'is_company_setup_complete': user.is_company_setup_complete,  # Ensure this is updated in DB
                'is_payroll_setup_complete': user.is_payroll_setup_complete,  # Fetch from CompanyDetails
                'company_id': company.companyId if company else None,  # Send company ID to the frontend
            }, status=200)
        return Response({"error": "Invalid credentials"}, status=401)


# class CompanyStatusView(APIView):
#     def get(self, request, user_id):
#         user = Login.objects.get(id=user_id)
#         if user.company:  # Ensure user has an associated company
#             company = user.company
#             company_status = {
#                     'company_setup_done': company.isCompanyDetailsCompleted,  # Ensure field exists in CompanyDetails
#                     'payroll_setup_done': company.payroll_done,  # Ensure field exists in CompanyDetails
#                     'employee_setup_done': company.employee_setup_done,  # Ensure field exists in CompanyDetails
#                 }
#             return Response(company_status, status=status.HTTP_200_OK)
#         return Response({"error": "Company setup not found"}, status=status.HTTP_404_NOT_FOUND)

#     def patch(self, request, user_id):
#         try:
#             user = Login.objects.get(id=user_id)

#             # Ensure the user has a company linked
#             if not user.company:
#                 return Response({"error": "User does not have a linked company"}, status=status.HTTP_400_BAD_REQUEST)

#             company = user.company

#             # Mark the company setup as done if it's part of the patch request
#             if 'setup_done' in request.data:
#                 company.isCompanyDetailsCompleted = request.data['setup_done']
#                 company.save()

#             # Mark the user's company setup as complete and update their role to admin
#             if 'is_company_setup_complete' in request.data:
#                 user.is_company_setup_complete = request.data['is_company_setup_complete']

#             if 'role' in request.data:
#                 user.role = request.data['role']  # Set role to 'admin'
            
#             user.save()

#             return Response({"message": "Company setup complete, user status updated"}, status=status.HTTP_200_OK)
        
#         except Login.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

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



# def patch(self, request, user_id):
#         try:

#             user = Login.objects.get(id=user_id)
#             company_id = request.data.get('company_id')
#             print(f"User ID: {user.id}, Company ID: {user.company_id}")  # Debugging log
#             print(f"Company ID: {company_id}")
#             # Ensure the user has a company linked
#             if not user.company:
#                 return Response({"error": "User does not have a linked company"}, status=status.HTTP_400_BAD_REQUEST)
            
#             company = CompanyDetails.objects.get(companyId=company_id)
#             company = user.company

#             # Mark the company setup as done if it's part of the patch request
#             if 'setup_done' in request.data:
#                 company.isCompanyDetailsCompleted = request.data['setup_done']
#                 company.save()

#             # Mark the user's company setup as complete and update their role to admin
#             if 'is_company_setup_complete' in request.data:
#                 user.is_company_setup_complete = request.data['is_company_setup_complete']

#             if 'role' in request.data:
#                 user.role = request.data['role']  # Set role to 'admin'
            
#             user.save()

#             return Response({"message": "Company setup complete, user status updated"}, status=status.HTTP_200_OK)
        
#         except Login.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
