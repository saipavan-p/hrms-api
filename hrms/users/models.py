#The original
# from django.db import models

# class Login(models.Model):
#     id = models.AutoField(primary_key=True)  
#     userName = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     phoneNum = models.CharField(max_length=15)

#     def __str__(self):
#         return self.userName

# The roles added
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, email, userName, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, userName=userName, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, userName, password=None, **extra_fields):
#         extra_fields.setdefault('is_admin', True)
#         extra_fields.setdefault('is_staff', True)
#         return self.create_user(email, userName, password, **extra_fields)

# class Login(AbstractBaseUser):
#     id = models.AutoField(primary_key=True)
#     userName = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     phoneNum = models.CharField(max_length=15)
#     company = models.ForeignKey('company.CompanyDetails', null=True, blank=True, on_delete=models.SET_NULL)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['userName']

#     objects = UserManager()

#     def __str__(self):
#         return self.userName

#new added roles
# from company.models import CompanyDetails

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, userName, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, userName=userName, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, userName, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, userName, password, **extra_fields)

class Login(AbstractBaseUser):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (EMPLOYEE, 'Employee'),
    ]

    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phoneNum = models.CharField(max_length=15)
    company = models.ForeignKey('company.CompanyDetails', null=True, blank=True, on_delete=models.SET_NULL)  # FK to CompanyDetails
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)
    is_admin = models.BooleanField(default=False)
    is_company_setup_complete = models.BooleanField(default=False)
    is_payroll_setup_complete = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userName']

    objects = UserManager()

    def __str__(self):
        return self.userName
