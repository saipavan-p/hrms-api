from rest_framework import serializers
from .models import EmpWorkDetails, EmpSocialSecurityDetails, EmpPersonalDetails, EmpInsuranceDetails

class EmpSocialSecurityDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpSocialSecurityDetails
        fields = '__all__'

class EmpPersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpPersonalDetails
        fields = '__all__'

class EmpInsuranceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpInsuranceDetails
        fields = '__all__'

class EmpWorkDetailsSerializer(serializers.ModelSerializer):
    social_security_details = serializers.PrimaryKeyRelatedField(queryset=EmpSocialSecurityDetails.objects.all(), required=False)
    personal_details = serializers.PrimaryKeyRelatedField(queryset=EmpPersonalDetails.objects.all(), required=False)
    insurance_details = serializers.PrimaryKeyRelatedField(queryset=EmpInsuranceDetails.objects.all(), required=False)

    class Meta:
        model = EmpWorkDetails
        fields = '__all__'

    def create(self, validated_data):
        # Simply create the work details record
        return EmpWorkDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Use default ModelSerializer update behavior for simplicity
        return super().update(instance, validated_data)
