# from rest_framework import serializers
# from .models import EmployeeCompensation

# class EmployeeCompensationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeCompensation
#         fields = '__all__'  # Includes all fields of EmployeeCompensation

#     def create(self, validated_data):
#         # Ensure that company field is passed and saved in the model
#         company = validated_data.get('company')  # Fetch the company field from validated_data
#         if not company:
#             raise serializers.ValidationError({"company": "This field may not be null."})
        
#         # Create the EmployeeCompensation entry with the validated data
#         return EmployeeCompensation.objects.create(**validated_data)

# from rest_framework import serializers
# from .models import EmployeeCompensation, Reimbursement


# class ReimbursementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reimbursement
#         fields = ['name', 'amount']

# class EmployeeCompensationSerializer(serializers.ModelSerializer):
#     reimbursements = ReimbursementSerializer(many=True)

#     class Meta:
#         model = EmployeeCompensation
#         fields = '__all__'  # Includes all fields of EmployeeCompensation

#     def create(self, validated_data):
#         # Ensure that company field is passed and saved in the model
#         company = validated_data.get('company')  # Fetch the company field from validated_data
#         if not company:
#             raise serializers.ValidationError({"company": "This field may not be null."})
        
#         # Create the EmployeeCompensation entry with the validated data
#         return EmployeeCompensation.objects.create(**validated_data)

# class EmployeeCompensationSerializer(serializers.ModelSerializer):
#     reimbursements = ReimbursementSerializer(many=True)

#     class Meta:
#         model = EmployeeCompensation
#         fields = '__all__'

#     def create(self, validated_data):
#         # Ensure that company field is passed and saved in the model
#         company = validated_data.get('company')  # Fetch the company field from validated_data
#         if not company:
#             raise serializers.ValidationError({"company": "This field may not be null."})
        
#         # Pop the reimbursements data if it exists
#         reimbursements_data = validated_data.pop('reimbursements', [])
        
#         # Create the EmployeeCompensation entry with the validated data
#         employee_compensation = EmployeeCompensation.objects.create(**validated_data)

#         # Create related reimbursements
#         for reimbursement_data in reimbursements_data:
#             Reimbursement.objects.create(employee_compensation=employee_compensation, **reimbursement_data)
        
#         return employee_compensation

from rest_framework import serializers
from .models import EmployeeCompensation
import json

# class EmployeeCompensationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeCompensation
#         fields = '__all__'

#     def create(self, validated_data):
#         # Extract reimbursements if present and store in validated_data
#         reimbursements = validated_data.pop('reimbursements', {})
#         instance = EmployeeCompensation.objects.create(
#             reimbursements=reimbursements,
#             **validated_data
#         )
#         return instance

class EmployeeCompensationSerializer(serializers.ModelSerializer):
    reimbursements = serializers.JSONField()
    class Meta:
        model = EmployeeCompensation
        fields = '__all__'

    def to_representation(self, instance):
        # Ensure that reimbursements is returned as a dictionary, even if stored as a string
        data = super().to_representation(instance)
        if isinstance(instance.reimbursements, str):
            data['reimbursements'] = json.loads(instance.reimbursements)
        return data

    def create(self, validated_data):
        reimbursements = validated_data.pop('reimbursements', {})
        
        # Create the EmployeeCompensation instance
        employee_compensation = EmployeeCompensation.objects.create(**validated_data)
        
        # Store reimbursements as a JSON field
        employee_compensation.reimbursements = reimbursements
        employee_compensation.save()
        
        return employee_compensation
