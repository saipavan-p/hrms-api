# from django.db import models
# from company.models import CompanyDetails

# class EmployeeCompensation(models.Model):
#     ecId = models.AutoField(primary_key=True)  

#     # Foreign key to CompanyDetails
#     # company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, related_name="compensations")
    
#     basic_percentage = models.FloatField() 
#     hra_percentage = models.FloatField()    
    
#     advances = models.BooleanField(default=False)  
#     variable_pay = models.BooleanField(default=False)  
#     deductions = models.BooleanField(default=False)  
#     # gratuity = models.BooleanField(default=False)  
#     quarterly_allowance = models.BooleanField(default=False)  
#     quarterly_bonus = models.BooleanField(default=False)  
#     annual_bonus = models.BooleanField(default=False)  
#     special_allowances = models.BooleanField(default=False)  
#     professional_tax = models.BooleanField(default=False)  
    
#     esi = models.BooleanField(default=False) 
#     # esi_percentage = models.FloatField(null=True, blank=True, choices=[
#     #     (0.75, "0.75% of monthly pay"), 
#     #     (3.25, "3.25% of monthly pay")
#     # ])  
    
#     pf = models.BooleanField(default=False)  
#     pf_type = models.CharField(max_length=10, null=True, blank=True, choices=[
#         (">15k", "Greater than 15k"),
#         ("<=15k", "Less than or equal to 15k"),
#         ("Both", "Both")
#     ])  # Only applicable if pf is True
#     voluntary_pf = models.CharField(max_length=10, null=True, blank=True, choices=[
#         ("No","VPF not applicable"),
#         ("Yes","VPF applicable")
#     ]) # Only applicable if pf is is >15K

    
#     def save(self, *args, **kwargs):
#         # Conditional logic for PF and ESI
#         if not self.pf:
#             self.pf_type = None
#             self.voluntary_pf = None  
#         else:
#         # Only check PF Type if PF is selected
#             if self.pf_type != ">15k":
#                 # If PF Type is not "Greater than 15k", clear Voluntary PF
#                 self.voluntary_pf = None
#         if not self.esi:
#             self.esi_percentage = None
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Compensation for Employee"



from django.db import models
from company.models import CompanyDetails

class EmployeeCompensation(models.Model):
    ecId = models.AutoField(primary_key=True)  

    # Foreign key to CompanyDetails
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, related_name="compensations")

    basic_percentage = models.FloatField() 
    hra_percentage = models.FloatField()    
    da_percentage = models.FloatField(null=True, blank=True)
    # Dynamic reimbursements stored as JSON
    reimbursements = models.JSONField(default=dict)  # Store key-value pairs for reimbursements

    advances = models.BooleanField(default=False)  
    variable_pay = models.BooleanField(default=False)  
    deductions = models.BooleanField(default=False)  
    quarterly_allowance = models.BooleanField(default=False)  
    quarterly_bonus = models.BooleanField(default=False)  
    annual_bonus = models.BooleanField(default=False)  
    special_allowances = models.BooleanField(default=False)  
    professional_tax = models.BooleanField(default=False)  
    
    esi = models.BooleanField(default=False) 
    pf = models.BooleanField(default=False)  
    pf_type = models.CharField(max_length=10, null=True, blank=True, choices=[
        ("!=15k", "No Limit for PF Deduction"),
        ("15k", "Wage limit 15k"),
        ("Both", "Both Options")
    ])  # Only applicable if pf is True
    # voluntary_pf = models.CharField(max_length=10, null=True, blank=True, choices=[
    #     ("No","VPF not applicable"),
    #     ("Yes","VPF applicable")
    # ]) # Only applicable if pf is is >15K

    voluntary_pf = models.BooleanField(default=False, null=True)

    is_payroll_generated = models.BooleanField(default=False)

    def __str__(self):
        return f"Compensation for Employee"


# class Reimbursement(models.Model):
#     employee_compensation = models.ForeignKey(EmployeeCompensation, related_name="reimbursements", on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

#     def __str__(self):
#         return f"{self.name} - {self.amount} Rs"