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
    attendance = models.IntegerField()
    lop_days = models.IntegerField()

    def __str__(self):
        return self.name
