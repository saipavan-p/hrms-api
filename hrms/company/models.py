from django.db import models
from users.models import Login  # Import your user model

class CompanyDetails(models.Model):
    companyId = models.AutoField(primary_key=True)  
    # Admin Info
    adminName = models.CharField(max_length=100)
    adminEmail = models.EmailField()
    adminPhoneNum = models.CharField(max_length=15)
    
    # Company Info
    companyName = models.CharField(max_length=100)
    companyRegisteredId = models.CharField(max_length=100)
    pan = models.CharField(max_length=20)
    tan = models.CharField(max_length=20)
    gst = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    coi = models.ImageField(upload_to='coi/', blank=True, null=True)   
    address = models.TextField()

    #Organization rules
    leavePolicy = models.FileField(upload_to='leave_policies/', blank=True, null=True)
    pfPolicy = models.FileField(upload_to='pf_policies/', blank=True, null=True)
    labourLawLicence = models.FileField(upload_to='labour_law_policies/', blank=True, null=True)

    # New ForeignKey to associate with a specific user
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='companies', null=True, blank=True)

    # Field to track whether the company details are completed
    is_company_details_completed = models.BooleanField(default=False)
    is_payroll_setup_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Company: {self.companyName}"




