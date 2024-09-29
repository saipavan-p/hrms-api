from django.db import models
from company.models import CompanyDetails

class EmployeeCompensation(models.Model):
    ecId = models.AutoField(primary_key=True)  

    # Foreign key to CompanyDetails
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, related_name="compensations")
    
    basic_percentage = models.FloatField() 
    hra_percentage = models.FloatField()    
    
    advances = models.BooleanField(default=False)  
    variable_pay = models.BooleanField(default=False)  
    deductions = models.BooleanField(default=False)  
    gratuity = models.BooleanField(default=False)  
    quarterly_allowance = models.BooleanField(default=False)  
    quarterly_bonus = models.BooleanField(default=False)  
    annual_bonus = models.BooleanField(default=False)  
    special_allowances = models.BooleanField(default=False)  
    professional_tax = models.BooleanField(default=False)  
    
    esi = models.BooleanField(default=False) 
    esi_percentage = models.FloatField(null=True, blank=True, choices=[
        (0.75, "0.75% of monthly pay"), 
        (3.25, "3.25% of monthly pay")
    ])  
    
    pf = models.BooleanField(default=False)  
    pf_type = models.CharField(max_length=10, null=True, blank=True, choices=[
        (">15k", "Greater than 15k"),
        ("<=15k", "Less than or equal to 15k"),
        ("vpf", "Voluntary Provident Fund")
    ])  # Only applicable if pf is True
    
    def save(self, *args, **kwargs):
        # Conditional logic for PF and ESI
        if not self.pf:
            self.pf_type = None
        if not self.esi:
            self.esi_percentage = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Compensation for Employee"
