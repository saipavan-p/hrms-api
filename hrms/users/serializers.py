from rest_framework import serializers
from .models import Login
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login  # Use the custom Login model
        fields = ['userName', 'email', 'password', 'phoneNum']

    def create(self, validated_data):
        # Create a new user object, hash the password before saving
        user = Login(
            userName=validated_data['userName'],
            email=validated_data['email'],
            phoneNum=validated_data['phoneNum']
        )
        user.password = self.make_password(validated_data['password'])  # Hash password manually
        user.save()
        return user

    def make_password(self, password):
        from django.contrib.auth.hashers import make_password
        return make_password(password)

class LoginSerializer(serializers.Serializer):
    userName = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = Login.objects.filter(userName=data['userName']).first()

        if user and self.check_password(data['password'], user.password):
            return user
        raise serializers.ValidationError("Invalid credentials")

    def check_password(self, raw_password, hashed_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, hashed_password)
