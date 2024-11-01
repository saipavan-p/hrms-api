# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import CompanyDetails
# from .serializers import CompanyDetailsSerializer

# class CompanyDetailsView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = CompanyDetailsSerializer(data=request.data)
#         if serializer.is_valid():
#             # Save the new company instance
#             company = serializer.save()
            
#             # Return response with companyId
#             return Response({
#                 "message": "Successfully submitted",
#                 "companyId": company.companyId  # Include companyId in the response
#             }, status=status.HTTP_201_CREATED)
        
#         # If validation fails, print errors and return bad request
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import CompanyDetails,Login
# from .serializers import CompanyDetailsSerializer, CompanyStatusSerializer

# class CompanyDetailsView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = CompanyDetailsSerializer(data=request.data)
#         if serializer.is_valid():
#             # Save the new company instance
#             company = serializer.save()
            
#             # Update completion status
#             status_serializer = CompanyStatusSerializer(company)
#             status_serializer.update(company, {'is_company_details_completed': True})

#             # Return response with companyId
#             return Response({
#                 "message": "Successfully submitted",
#                 "companyId": company.companyId  # Include companyId in the response
#             }, status=status.HTTP_201_CREATED)
        
#         # If validation fails, print errors and return bad request
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# # class CompanySetupView(APIView):
# #     def post(self, request):
# #         # Company details are received from the request
# #         company_data = request.data.get('company')

# #         # Create or update company details
# #         company = CompanyDetails.objects.create(
# #             company_name=company_data['name'], 
# #             company_registered_id=company_data['registered_id'],
# #             address=company_data['address'],
# #             # Other fields
# #         )

# #         # The company instance is created, and the company ID is now available
# #         company_id = company.id

# #         # Send the company ID to update the user's Login model
# #         user = request.user  # Assuming the user is logged in
# #         user.company = company  # Set the ForeignKey to the company
# #         user.is_company_setup_complete = True  # Mark the setup as complete
# #         user.role = 'admin'  # Update user role to admin
# #         user.save()

# #         return Response({
# #             "message": "Company setup complete",
# #             "companyId": company_id  # Returning the company ID in the response
# #         }, status=status.HTTP_201_CREATED)

# class CompanySetupView(APIView):
#     def post(self, request):
#         user = request.user  # Get the logged-in user

#         # Create a new company instance
#         company = CompanyDetails.objects.create(
#             companyName=request.data['companyName'],
#             companyRegisteredId=request.data['companyRegisteredId'],
#             address=request.data['address'],
#             adminName=request.data['adminName'],
#             adminEmail=request.data['adminEmail'],
#             adminPhoneNum=request.data['adminPhoneNum'],
#             admin=user,  # Assign the user as the admin of the company
#             gst=request.data.get('gst'),
#             pan=request.data.get('pan'),
#             tan=request.data.get('tan'),
#             logo=request.FILES.get('logo'),
#             leavePolicy=request.FILES.get('leavePolicy'),
#             pfPolicy=request.FILES.get('pfPolicy'),
#             labourLawLicence=request.FILES.get('labourLawLicence')
#         )

#         # Mark company setup as complete
#         company.isCompanyDetailsCompleted = True
#         company.save()

#         # Update the user with the created company ID
#         user.company = company
#         user.is_company_setup_complete = True
#         user.role = 'admin'
#         user.save()

#         return Response({"companyId": company.companyId, "message": "Company setup complete and admin details saved"}, status=status.HTTP_201_CREATED)


from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CompanyDetails  # No need to import Login here
from .serializers import CompanyDetailsSerializer, CompanyDetailsGetSerializer
from users.models import Login  # Assuming your user model is called Login

class CompanyDetailsView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CompanyDetailsSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new company instance
            company = serializer.save()
            
            # Mark company setup as complete
            company.isCompanyDetailsCompleted = True
            company.save()

            # Return response with companyId
            return Response({
                "message": "Successfully submitted",
                "companyId": company.companyId  # Include companyId in the response
            }, status=status.HTTP_201_CREATED)
        
        # If validation fails, return bad request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanySetupView(APIView):
    def post(self, request):
        # Get the user_id from the request data
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new company instance
        company = CompanyDetails.objects.create(
            user_id=user_id,  # Assign the user as the admin of the company
            companyName=request.data['companyName'],
            companyRegisteredId=request.data['companyRegisteredId'],
            address=request.data['address'],
            adminName=request.data['adminName'],
            adminEmail=request.data['adminEmail'],
            adminPhoneNum=request.data['adminPhoneNum'],
            gst=request.data.get('gst'),
            pan=request.data.get('pan'),
            tan=request.data.get('tan'),
            logo=request.FILES.get('logo'),
            leavePolicy=request.FILES.get('leavePolicy'),
            pfPolicy=request.FILES.get('pfPolicy'),
            labourLawLicence=request.FILES.get('labourLawLicence')
        )

        # Mark company setup as complete
        company.isCompanyDetailsCompleted = True
        company.save()

        # Update the user with the created company ID
        user.company = company  # Link the company to the user in the Login model
        user.is_company_setup_complete = True
        user.role = 'admin'
        user.save()
        print(f"User {user.id} linked to Company {user.company_id}") 

        return Response({"companyId": company.companyId, "message": "Company setup complete and admin details saved"}, status=status.HTTP_201_CREATED)


class CompanyDetailRetrieveView(APIView):
    def get(self, request, companyId):
        try:
            # Fetch the company using companyId
            company = CompanyDetails.objects.get(companyId=companyId)
            serializer = CompanyDetailsGetSerializer(company)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CompanyDetails.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateCompanyDetailsView(APIView):
    # permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def put(self, request, companyId):
        try:
            company = CompanyDetails.objects.get(companyId=companyId)
            serializer = CompanyDetailsSerializer(company, data=request.data, partial=True)  # Use partial=True for partial updates

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

                # return Response({"message": "Company details updated successfully", "companyId": companyId}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CompanyDetails.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)