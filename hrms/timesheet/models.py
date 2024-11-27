from django.db import models
from employee.models import EmpWorkDetails
from company.models import CompanyDetails 

class TimeSheet(models.Model):
    tsId = models.AutoField(primary_key=True)
    empId = models.ForeignKey(EmpWorkDetails, on_delete=models.CASCADE, to_field='empId',null=True,blank=True)  # FK to Employee.emp_id
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)  # FK to Company model
    # empId = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    month = models.CharField(max_length=20)
    no_of_days = models.IntegerField()
    attendance = models.FloatField()
    lop_days = models.FloatField()
    OT = models.FloatField(default=0)
    allowance = models.IntegerField(default=0)
    deductions = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class PayCalculation(models.Model):
    tsId = models.AutoField(primary_key=True)
    empId = models.ForeignKey(
        EmpWorkDetails, on_delete=models.CASCADE, to_field='empId', null=True, blank=True
    )  # FK to Employee.emp_id
    company = models.ForeignKey(
        CompanyDetails, on_delete=models.CASCADE, null=True, blank=True
    )  # FK to Company model

    # Basic fields from the timesheet
    name = models.CharField(max_length=255)
    month = models.CharField(max_length=20)
    no_of_days = models.IntegerField()
    attendance = models.FloatField()
    lop_days = models.FloatField()
    OT = models.FloatField(default=0)
    

    # Salary and calculation fields
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # CTCpayAMT
    basic = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2)
    da = models.DecimalField(max_digits=10, decimal_places=2)
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    grossPay = models.DecimalField(max_digits=10, decimal_places=2)
    otPay = models.DecimalField(max_digits=10, decimal_places=2)
    allowance = models.DecimalField(max_digits=10, decimal_places=2)
    totalPay = models.DecimalField(max_digits=10, decimal_places=2)
    eePF = models.DecimalField(max_digits=10, decimal_places=2)  # Employee Provident Fund
    esi = models.DecimalField(max_digits=10, decimal_places=2)  # Employee State Insurance
    pt = models.DecimalField(max_digits=10, decimal_places=2)  # Professional Tax
    deductiblesLoans = models.DecimalField(max_digits=10, decimal_places=2)  # DLoansAMT
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.month}'



# class Attendance(models.Model):
#     aId = models.AutoField(primary_key=True)
#     empId = models.ForeignKey(EmpWorkDetails, on_delete=models.CASCADE, to_field='empId',null=True,blank=True)  # FK to Employee.emp_id
#     company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)  # FK to Company model
#     department = models.CharField(max_length=255)
#     # emp_id = models.CharField(max_length=50)
#     name = models.CharField(max_length=255)
#     month = models.CharField(max_length=20)  # Example: "Oct 2024"
#     no_of_days = models.IntegerField()
#     attendance = models.IntegerField()
#     lop_days = models.IntegerField()
#     present_days = models.IntegerField()
#     wo_days = models.IntegerField()
#     wop_days = models.IntegerField()
    
#     def __str__(self):
#         return f"{self.emp_id} - {self.name} ({self.month})"