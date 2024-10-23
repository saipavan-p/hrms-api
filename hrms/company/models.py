# from django.db import models
# from users.models import Login  # Import your user model

# class CompanyDetails(models.Model):
#     companyId = models.AutoField(primary_key=True)  
#     # Admin Info
#     adminName = models.CharField(max_length=100)
#     adminEmail = models.EmailField()
#     adminPhoneNum = models.CharField(max_length=15)
    
#     # Company Info
#     companyName = models.CharField(max_length=100)
#     companyRegisteredId = models.CharField(max_length=100)
#     pan = models.CharField(max_length=20)
#     tan = models.CharField(max_length=20)
#     gst = models.CharField(max_length=20)
#     logo = models.ImageField(upload_to='logos/', blank=True, null=True)
#     coi = models.ImageField(upload_to='coi/', blank=True, null=True)   
#     address = models.TextField()

#     #Organization rules
#     leavePolicy = models.FileField(upload_to='leave_policies/', blank=True, null=True)
#     pfPolicy = models.FileField(upload_to='pf_policies/', blank=True, null=True)
#     labourLawLicence = models.FileField(upload_to='labour_law_policies/', blank=True, null=True)

#     # New ForeignKey to associate with a specific user
#     user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='companies', null=True, blank=True)

#     # Field to track whether the company details are completed
#     is_company_details_completed = models.BooleanField(default=False)
#     is_payroll_setup_completed = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Company: {self.companyName}"




# from django.db import models
# from users.models import Login  # Import your user model

# class CompanyDetails(models.Model):
#     companyId = models.AutoField(primary_key=True)
    
#     # Admin Info
#     adminName = models.CharField(max_length=100)
#     adminEmail = models.EmailField()
#     adminPhoneNum = models.CharField(max_length=15)
    
#     # Company Info
#     companyName = models.CharField(max_length=100)
#     companyRegisteredId = models.CharField(max_length=100)
#     pan = models.CharField(max_length=20)
#     tan = models.CharField(max_length=20)
#     gst = models.CharField(max_length=20)
#     logo = models.ImageField(upload_to='logos/', blank=True, null=True)
#     coi = models.ImageField(upload_to='coi/', blank=True, null=True)
#     address = models.TextField()
    
#     # Organizational rules
#     leavePolicy = models.FileField(upload_to='leave_policies/', blank=True, null=True)
#     pfPolicy = models.FileField(upload_to='pf_policies/', blank=True, null=True)
#     labourLawLicence = models.FileField(upload_to='labour_law_policies/', blank=True, null=True)
    
#     # Foreign Key to associate the company with a specific user (the admin)
#     user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='companies', null=True, blank=True)
    
#     # Fields to track whether the company details are completed
#     is_company_details_completed = models.BooleanField(default=False)
#     is_payroll_setup_completed = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Company: {self.companyName}"
    




from django.db import models
from users.models import Login 


class CompanyDetails(models.Model):
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=255)
    companyRegisteredId = models.CharField(max_length=255, unique=True)
    address = models.TextField()

    # Admin Details
    adminName = models.CharField(max_length=255)
    adminEmail = models.EmailField()
    adminPhoneNum = models.CharField(max_length=15)

    # Foreign key for linking admin user from the Login model
    # user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='company_admin', null=True, blank=True)
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    # Optional fields for additional data
    gst = models.CharField(max_length=15, blank=True, null=True)
    pan = models.CharField(max_length=10, blank=True, null=True)
    tan = models.CharField(max_length=10, blank=True, null=True)
    coi = models.ImageField(upload_to='coi/', blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    leavePolicy = models.FileField(upload_to='leave_policies/', blank=True, null=True)
    pfPolicy = models.FileField(upload_to='pf_policies/', blank=True, null=True)
    labourLawLicence = models.FileField(upload_to='labour_law_policies/', blank=True, null=True)

    # Setup progress flags
    isCompanyDetailsCompleted = models.BooleanField(default=False)
    payrollDone = models.BooleanField(default=False)
    employeeSetupDone = models.BooleanField(default=False)

    def __str__(self):
        return self.companyName

