# from rest_framework import viewsets
# from .models import EmployeeCompensation
# from rest_framework.response import Response
# from rest_framework import status

# from .serializers import EmployeeCompensationSerializer

# class EmployeeCompensationViewSet(viewsets.ModelViewSet):
#     queryset = EmployeeCompensation.objects.all()
#     serializer_class = EmployeeCompensationSerializer

#     def create(self, request, *args, **kwargs):
#         company_id = request.data.get('company')
#         if not company_id:
#             return Response({"company": ["This field may not be null."]}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Handle creation
#         return super().create(request, *args, **kwargs)


# from rest_framework import viewsets
# from .models import EmployeeCompensation
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import EmployeeCompensationSerializer

# class EmployeeCompensationViewSet(viewsets.ModelViewSet):
#     queryset = EmployeeCompensation.objects.all()
#     serializer_class = EmployeeCompensationSerializer

#     def create(self, request, *args, **kwargs):
#         company_id = request.data.get('company')
#         if not company_id:
#             return Response({"company": ["This field may not be null."]}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Handle creation
#         return super().create(request, *args, **kwargs)
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework import viewsets
# from .models import EmployeeCompensation
# from .serializers import EmployeeCompensationSerializer

# class EmployeeCompensationViewSet(viewsets.ModelViewSet):
#     queryset = EmployeeCompensation.objects.all()
#     serializer_class = EmployeeCompensationSerializer

#     def create(self, request, *args, **kwargs):
#         # Fetch the company ID from the request data
#         company_id = request.data.get('company')
        
#         # Ensure the company field is present
#         if not company_id:
#             return Response({"company": ["This field may not be null."]}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Call the parent class's create method to handle creation
#         response = super().create(request, *args, **kwargs)
        
#         # After the EmployeeCompensation instance is created, update the is_payroll_generated field
#         compensation = self.get_object()  # Get the newly created object
#         compensation.is_payroll_generated = True  # Set the payroll generation flag
#         compensation.save()

#         return response

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import EmployeeCompensation
from .serializers import EmployeeCompensationSerializer
from company.models import CompanyDetails
from users.models import Login  # Import Login model
import json

# class EmployeeCompensationViewSet(viewsets.ModelViewSet):
#     queryset = EmployeeCompensation.objects.all()
#     serializer_class = EmployeeCompensationSerializer

#     def create(self, request, *args, **kwargs):
#         # Call the parent class's create method to handle creation
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         compensation = serializer.save()  # Save the object and return the instance
        
#         # Get companyId from the created compensation object (ForeignKey)
#         company_id = compensation.company.companyId  # Use 'companyId' as the primary key

#         # Mark payroll as generated
#         compensation.is_payroll_generated = True
#         compensation.save()

#         # Update the company's payroll setup status
#         company = CompanyDetails.objects.get(companyId=company_id)  # Use 'companyId' for fetching the company
#         company.is_payroll_setup_complete = True  # Set payroll setup complete for the company
#         company.save()

#         # Option A: Update payroll setup flag for all users associated with the company
#         Login.objects.filter(company_id=company_id).update(is_payroll_setup_complete=True)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    


# class PayrollSettingsView(APIView):
#     def get(self, request, company_id):
#         try:
#             # Use the correct field 'companyId' (with capital I)
#             company = CompanyDetails.objects.get(companyId=company_id)

#             payroll_settings = EmployeeCompensation.objects.filter(company=company).first()

#             if not payroll_settings:
#                 return Response({"error": "No payroll settings found for this company."}, status=status.HTTP_404_NOT_FOUND)

#             # Serialize and return the payroll settings
#             serializer = EmployeeCompensationSerializer(payroll_settings)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         except CompanyDetails.DoesNotExist:
#             return Response({"error": "Company not found."}, status=status.HTTP_404_NOT_FOUND)

class EmployeeCompensationViewSet(viewsets.ModelViewSet):
    queryset = EmployeeCompensation.objects.all()
    serializer_class = EmployeeCompensationSerializer

    def create(self, request, *args, **kwargs):
        # Process reimbursements and store as key-value pairs (name -> amount)
        reimbursements = {
            request.data.get('reimbursement1'): request.data.get('amount1'),
            request.data.get('reimbursement2'): request.data.get('amount2'),
            request.data.get('reimbursement3'): request.data.get('amount3'),
            request.data.get('reimbursement4'): request.data.get('amount4'),
        }

        # Filter out any None or empty reimbursements
        reimbursements = {k: v for k, v in reimbursements.items() if k and v}

        # Merge reimbursement data into request data
        request.data['reimbursements'] = reimbursements

        # Call the parent class's create method to handle creation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        compensation = serializer.save()

        # Get companyId from the created compensation object
        company_id = compensation.company.companyId

        # Mark payroll as generated
        compensation.is_payroll_generated = True
        compensation.save()

        # Update the company's payroll setup status
        company = CompanyDetails.objects.get(companyId=company_id)
        company.is_payroll_setup_complete = True
        company.save()

        # Option A: Update payroll setup flag for all users associated with the company
        Login.objects.filter(company_id=company_id).update(is_payroll_setup_complete=True)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class PayrollSettingsView(APIView):
    def get(self, request, company_id):
        try:
            # Use the correct field 'companyId' (with capital I)
            company = CompanyDetails.objects.get(companyId=company_id)

            # payroll_settings = EmployeeCompensation.objects.filter(company=company).first()

            payroll_settings = EmployeeCompensation.objects.filter(company=company).order_by('-ecId').first()

            if not payroll_settings:
                return Response({"error": "No payroll settings found for this company."}, status=status.HTTP_404_NOT_FOUND)

            # Serialize and return the payroll settings
            serializer = EmployeeCompensationSerializer(payroll_settings)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except CompanyDetails.DoesNotExist:
            return Response({"error": "Company not found."}, status=status.HTTP_404_NOT_FOUND)
