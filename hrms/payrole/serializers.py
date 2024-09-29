from rest_framework import serializers
from .models import EmployeeCompensation

class EmployeeCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCompensation
        fields = '__all__'  # Includes all fields of EmployeeCompensation

