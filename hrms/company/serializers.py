# from rest_framework import serializers
# from .models import CompanyDetails

# class CompanyDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CompanyDetails
#         fields = '__all__'

   

# from rest_framework import serializers
# from .models import CompanyDetails

# class CompanyDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CompanyDetails
#         # fields = '__all__'
#         fields = ['companyName', 'companyRegisteredId', 'address', 'gst', 'pan', 'tan','coi', 'logo', 'leavePolicy', 'pfPolicy'] 

# class CompanyStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CompanyDetails  # Replace with your actual model name
#         fields = ['isCompanyDetailsCompleted']

#     def update(self, instance, validated_data):
#         instance.is_company_details_completed = validated_data.get('isCompanyDetailsCompleted', instance.is_company_details_completed)
#         instance.is_payroll_setup_completed = validated_data.get('is_payroll_setup_completed', instance.is_payroll_setup_completed)
#         instance.save()
#         return instance
from rest_framework import serializers
from .models import CompanyDetails

class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = [
            'companyName', 'companyRegisteredId', 'address', 
            'adminName', 'adminEmail', 'adminPhoneNum', 
            'gst', 'pan', 'tan', 'logo', 
            'leavePolicy', 'pfPolicy', 'labourLawLicence'
        ]

class CompanyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = ['isCompanyDetailsCompleted', 'payrollDone', 'employeeSetupDone']  # Fixed field names

    def update(self, instance, validated_data):
        instance.isCompanyDetailsCompleted = validated_data.get('isCompanyDetailsCompleted', instance.isCompanyDetailsCompleted)
        instance.payrollDone = validated_data.get('payrollDone', instance.payrollDone)
        instance.employeeSetupDone = validated_data.get('employeeSetupDone', instance.employeeSetupDone)
        instance.save()
        return instance
