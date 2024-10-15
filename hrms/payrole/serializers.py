from rest_framework import serializers
from .models import EmployeeCompensation

class EmployeeCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCompensation
        fields = '__all__'  # Includes all fields of EmployeeCompensation

    def create(self, validated_data):
        # Ensure that company field is passed and saved in the model
        company = validated_data.get('company')  # Fetch the company field from validated_data
        if not company:
            raise serializers.ValidationError({"company": "This field may not be null."})
        
        # Create the EmployeeCompensation entry with the validated data
        return EmployeeCompensation.objects.create(**validated_data)
