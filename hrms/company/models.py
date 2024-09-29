from django.db import models

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

    def __str__(self):
        return f"Company: {self.companyName}"




