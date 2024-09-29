# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from django.db import transaction
# from django.shortcuts import get_object_or_404

# from .models import EmpWorkDetails, EmpSocialSecurityDetails, EmpPersonalDetails, EmpInsuranceDetails
# from .serializers import (
#     EmpWorkDetailsSerializer, 
#     EmpSocialSecurityDetailsSerializer, 
#     EmpPersonalDetailsSerializer, 
#     EmpInsuranceDetailsSerializer
# )

# class CombinedDetailsViewSet(viewsets.ViewSet):
#     @transaction.atomic
#     def create(self, request):
#         work_data = request.data.get('work_details')
#         print(work_data)
#         social_security_data = request.data.get('social_security_details')
#         print(social_security_data)
#         personal_data = request.data.get('personal_details')
#         print(personal_data)
#         insurance_data = request.data.get('insurance_details')
#         print(insurance_data)

#         # Step 1: Validate and save EmpWorkDetails
#         work_serializer = EmpWorkDetailsSerializer(data=work_data)
#         if not work_serializer.is_valid():
#             return Response({
#                 "message": "Validation errors occurred.",
#                 "work_details_errors": work_serializer.errors,
#                 "social_security_details_errors": {},
#                 "personal_details_errors": {},
#                 "insurance_details_errors": {}
#             }, status=status.HTTP_400_BAD_REQUEST)
        

#         work_instance = work_serializer.save()
#         print("work instance",work_instance)

#         try:
#             # Step 2: Validate and save EmpSocialSecurityDetails
#             social_security_data['wdId'] = work_instance.pk
#             social_security_serializer = EmpSocialSecurityDetailsSerializer(data=social_security_data)
#             if not social_security_serializer.is_valid():
#                 raise ValueError("Social security validation failed")

#             social_security_instance = social_security_serializer.save()
#             print("Social security instace",social_security_instance)

#             # Step 3: Validate and save EmpPersonalDetails
#             personal_data['wdId'] = work_instance.pk
#             personal_serializer = EmpPersonalDetailsSerializer(data=personal_data)
#             if not personal_serializer.is_valid():
#                 raise ValueError("Personal details validation failed")

#             personal_instance = personal_serializer.save()

#             # Step 4: Validate and save EmpInsuranceDetails
#             insurance_data['wdId'] = work_instance.pk
#             insurance_serializer = EmpInsuranceDetailsSerializer(data=insurance_data)
#             if not insurance_serializer.is_valid():
#                 raise ValueError("Insurance details validation failed")

#             insurance_instance = insurance_serializer.save()

#         except ValueError as e:
#             # If any validation fails, roll back the transaction
#             transaction.set_rollback(True)
#             return Response({
#                 "message": "Validation errors occurred.",
#                 "work_details_errors": {},
#                 "social_security_details_errors": social_security_serializer.errors if social_security_serializer else {},
#                 "personal_details_errors": personal_serializer.errors if personal_serializer else {},
#                 "insurance_details_errors": insurance_serializer.errors if insurance_serializer else {}
#             }, status=status.HTTP_400_BAD_REQUEST)

#         return Response({
#             "message": "Successfully submitted all details."
#         }, status=status.HTTP_201_CREATED)

        # return Response({
        #     "work_details": work_serializer.data,
        #     "social_security_details": social_security_serializer.data,
        #     "personal_details": personal_serializer.data,
        #     "insurance_details": insurance_serializer.data
        # }, status=status.HTTP_201_CREATED)


from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404

from .models import EmpWorkDetails, EmpSocialSecurityDetails, EmpPersonalDetails, EmpInsuranceDetails
from .serializers import (
    EmpWorkDetailsSerializer, 
    EmpSocialSecurityDetailsSerializer, 
    EmpPersonalDetailsSerializer, 
    EmpInsuranceDetailsSerializer
)

class CombinedDetailsViewSet(viewsets.ViewSet):
    @transaction.atomic
    def create(self, request):
        work_data = request.data.get('work_details')
        print("Work Data:",work_data)
        social_security_data = request.data.get('social_security_details')
        print("Social Data:",social_security_data)
        personal_data = request.data.get('personal_details')
        print("Personal data:",personal_data)
        insurance_data = request.data.get('insurance_details')
        print("Insurance data:",insurance_data)

        # # Initialize serializers
        # work_serializer = EmpWorkDetailsSerializer(data=work_data)
        # social_security_serializer = EmpSocialSecurityDetailsSerializer()
        # personal_serializer = EmpPersonalDetailsSerializer()
        # insurance_serializer = EmpInsuranceDetailsSerializer()

        # Step 1: Validate and save EmpWorkDetails
        work_serializer = EmpWorkDetailsSerializer(data=work_data)
        if not work_serializer.is_valid():
            return Response({
                "message": "Validation errors occurred.",
                "work_details_errors": work_serializer.errors,
                "social_security_details_errors": {},
                "personal_details_errors": {},
                "insurance_details_errors": {}
            }, status=status.HTTP_400_BAD_REQUEST)
        
        work_instance = work_serializer.save()
        print("work instance",work_instance)

        try:
            # Step 2: Validate and save EmpSocialSecurityDetails
            social_security_data['wdId'] = work_instance.pk
            social_security_serializer = EmpSocialSecurityDetailsSerializer(data=social_security_data)
            if not social_security_serializer.is_valid():
                raise ValueError("Social security validation failed")
            social_security_instance = social_security_serializer.save()
            print("social",social_security_instance)

            # Step 3: Validate and save EmpPersonalDetails
            personal_data['wdId'] = work_instance.pk
            personal_serializer = EmpPersonalDetailsSerializer(data=personal_data)
            if not personal_serializer.is_valid():
                raise ValueError("Personal details validation failed")
            personal_instance = personal_serializer.save()
            print(personal_instance)

            # Step 4: Validate and save EmpInsuranceDetails
            insurance_data['wdId'] = work_instance.pk
            insurance_serializer = EmpInsuranceDetailsSerializer(data=insurance_data)
            if not insurance_serializer.is_valid():
                raise ValueError("Insurance details validation failed")
            insurance_instance = insurance_serializer.save()
            print(insurance_instance)

        except ValueError as e:
            # If any validation fails, roll back the transaction
            transaction.set_rollback(True)
            return Response({
                "message": "Validation errors occurred.",
                "work_details_errors": {},
                "social_security_details_errors": social_security_serializer.errors if 'social_security_serializer' in locals() else {},
                "personal_details_errors": personal_serializer.errors if 'personal_serializer' in locals() else {},
                "insurance_details_errors": insurance_serializer.errors if 'insurance_serializer' in locals() else {}
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Successfully submitted all details."
        }, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        work_instance = get_object_or_404(EmpWorkDetails, pk=pk)
        social_security_instance = get_object_or_404(EmpSocialSecurityDetails, wdId=work_instance)
        personal_instance = get_object_or_404(EmpPersonalDetails, wdId=work_instance)
        insurance_instance = get_object_or_404(EmpInsuranceDetails, wdId=work_instance)

        work_serializer = EmpWorkDetailsSerializer(work_instance)
        social_security_serializer = EmpSocialSecurityDetailsSerializer(social_security_instance)
        personal_serializer = EmpPersonalDetailsSerializer(personal_instance)
        insurance_serializer = EmpInsuranceDetailsSerializer(insurance_instance)

        response_data = {
            "work_details": work_serializer.data,
            "social_security_details": social_security_serializer.data,
            "personal_details": personal_serializer.data,
            "insurance_details": insurance_serializer.data
        }
        return Response(response_data)

    @transaction.atomic
    def partial_update(self, request, pk=None):
        # Use correct model name
        work_instance = get_object_or_404(EmpWorkDetails, pk=pk)

        # Extract and validate data
        company_data = request.data.get('work_details', {})
        personal_data = request.data.get('personal_details', {})
        social_security_data = request.data.get('social_security_details', {})
        insurance_data = request.data.get('insurance_details', {})

        # Validate and update work details
        work_serializer = EmpWorkDetailsSerializer(work_instance, data=company_data, partial=True)
        if not work_serializer.is_valid():
            return Response({
                "message": "Validation errors occurred.",
                "work_details_errors": work_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        work_instance = work_serializer.save()

        # Validate and update personal details
        personal_instance = get_object_or_404(EmpPersonalDetails, wdId=work_instance)
        personal_serializer = EmpPersonalDetailsSerializer(personal_instance, data=personal_data, partial=True)
        if not personal_serializer.is_valid():
            return Response({
                "message": "Validation errors occurred.",
                "personal_details_errors": personal_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        personal_instance = personal_serializer.save()

        # Validate and update social security details
        social_security_instance = get_object_or_404(EmpSocialSecurityDetails, wdId=work_instance)
        social_security_serializer = EmpSocialSecurityDetailsSerializer(social_security_instance, data=social_security_data, partial=True)
        if not social_security_serializer.is_valid():
            return Response({
                "message": "Validation errors occurred.",
                "social_security_details_errors": social_security_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        social_security_instance = social_security_serializer.save()

        # Validate and update insurance details
        insurance_instance = get_object_or_404(EmpInsuranceDetails, wdId=work_instance)
        insurance_serializer = EmpInsuranceDetailsSerializer(insurance_instance, data=insurance_data, partial=True)
        if not insurance_serializer.is_valid():
            return Response({
                "message": "Validation errors occurred.",
                "insurance_details_errors": insurance_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        insurance_instance = insurance_serializer.save()

        # Return updated data
        return Response({
            "work_details": work_serializer.data,
            "social_security_details": social_security_serializer.data,
            "personal_details": personal_serializer.data,
            "insurance_details": insurance_serializer.data
        }, status=status.HTTP_200_OK)


    @transaction.atomic
    def destroy(self, request, pk=None):
        # Check if the work details exist
        work_instance = EmpWorkDetails.objects.filter(pk=pk).first()

        if not work_instance:
            return Response({
                "message": "Item not found."
            }, status=status.HTTP_404_NOT_FOUND)

        # If found, get related details and delete all
        social_security_instance = EmpSocialSecurityDetails.objects.filter(wdId=work_instance).first()
        personal_instance = EmpPersonalDetails.objects.filter(wdId=work_instance).first()
        insurance_instance = EmpInsuranceDetails.objects.filter(wdId=work_instance).first()

        if social_security_instance:
            social_security_instance.delete()
        if personal_instance:
            personal_instance.delete()
        if insurance_instance:
            insurance_instance.delete()
    
        work_instance.delete()

        return Response({
            "message": "Successfully deleted."
        }, status=status.HTTP_200_OK)

    def list(self, request):
        # Retrieve all employee work details
        work_instances = EmpWorkDetails.objects.all()

        # Initialize lists for serialized data
        work_details_list = []
        social_security_details_list = []
        personal_details_list = []
        insurance_details_list = []

        for work_instance in work_instances:
            # Serialize and add work details
            work_serializer = EmpWorkDetailsSerializer(work_instance)
            work_data = work_serializer.data

            # Retrieve related data
            social_security_instance = EmpSocialSecurityDetails.objects.filter(wdId=work_instance).first()
            personal_instance = EmpPersonalDetails.objects.filter(wdId=work_instance).first()
            insurance_instance = EmpInsuranceDetails.objects.filter(wdId=work_instance).first()

            # Serialize and add related details if they exist
            social_security_data = {}
            personal_data = {}
            insurance_data = {}

            if social_security_instance:
                social_security_serializer = EmpSocialSecurityDetailsSerializer(social_security_instance)
                social_security_data = social_security_serializer.data

            if personal_instance:
                personal_serializer = EmpPersonalDetailsSerializer(personal_instance)
                personal_data = personal_serializer.data

            if insurance_instance:
                insurance_serializer = EmpInsuranceDetailsSerializer(insurance_instance)
                insurance_data = insurance_serializer.data

            # Combine all details into one dictionary
            combined_data = {
                "work_details": work_data,
                "social_security_details": social_security_data,
                "personal_details": personal_data,
                "insurance_details": insurance_data
            }

            # Add the combined data to the lists
            work_details_list.append(combined_data)

        response_data = {
            "employees": work_details_list
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
