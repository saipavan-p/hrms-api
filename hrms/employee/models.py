from django.db import models
from company.models import CompanyDetails
from payrole.models import EmployeeCompensation

# Employee Work Details
class EmpWorkDetails(models.Model):
    wdId = models.AutoField(primary_key=True)  # Primary key for the work details

    # Foreign Key to CompanyDetails
    # company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE, related_name="employees")

    # # Foreign Key to EmployeeCompensation (Compensation structure that applies to this employee)
    # compensation = models.ForeignKey(EmployeeCompensation, on_delete=models.CASCADE, related_name="employees")

    # Employee-specific fields
    empId = models.CharField(max_length=255, unique=True)  # Unique employee ID
    employmentStatus = models.CharField(max_length=100)  # Employment status (e.g., Active, Terminated)
    companyEmailId = models.EmailField()  # Employee's official email ID
    dateOfJoining = models.DateField()  # Date of joining
    dateOfRelieving = models.DateField(null=True, blank=True)  # Date of relieving (if applicable)

    firstName = models.CharField(max_length=100)  # First name of employee
    lastName = models.CharField(max_length=100)  # Last name of employee
    group = models.CharField(max_length=100, null=True, blank=True)  # Group (optional)
    department = models.CharField(max_length=100)  # Department of the employee
    roleType = models.CharField(max_length=100)  # Type of role (e.g., Permanent, Contractual)
    currentRole = models.CharField(max_length=100)  # Current role (designation) of the employee
    reportingManager = models.CharField(max_length=100)  # Reporting manager's name
    reasonForLeaving = models.TextField(null=True, blank=True)  # Reason for leaving (if applicable)

    monthYearOfTermination = models.CharField(max_length=100, null=True, blank=True)
    # Experience and Termination details
    totalExpInThisCompany = models.CharField(max_length=100, null=True, blank=True)
    totalExperience = models.CharField(max_length=100, null=True, blank=True)
    totalExpBeforeJoining = models.CharField(max_length=100, null=True, blank=True)
    
    previousDateOfJoining = models.DateField(null=True, blank=True)
    previousEmployer = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Work details for {self.firstName} {self.lastName} (Employee ID: {self.empId})"


# Employee Social Security Details
class EmpSocialSecurityDetails(models.Model):
    ssdId = models.AutoField(primary_key=True)
    wdId = models.ForeignKey(EmpWorkDetails, on_delete=models.CASCADE)
    panNum = models.CharField(max_length=20)
    uanNum = models.CharField(max_length=20)
    aadharNum = models.CharField(max_length=20)
    bankName = models.CharField(max_length=100)
    ifscCode = models.CharField(max_length=20)
    bankAccountNumber = models.CharField(max_length=50)

    def __str__(self):
        return f"Social Security Details for {self.wdId.empId}"


# Employee Personal Details
class EmpPersonalDetails(models.Model):
    pdId = models.AutoField(primary_key=True)
    wdId = models.ForeignKey(EmpWorkDetails, on_delete=models.CASCADE)
    personalEmailId = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    educationalQualification = models.CharField(max_length=100)
    maritalStatus = models.CharField(max_length=50)
    marriageDate = models.DateField(null=True, blank=True)
    currentAddress = models.TextField()
    permanentAddress = models.TextField()
    generalContact = models.TextField(null=True, blank=True)
    emergencyContact = models.TextField(null=True, blank=True)
    relationship = models.CharField(max_length=100)
    relationshipName = models.CharField(max_length=100)
    bloodGroup = models.CharField(max_length=10)
    shirtSize = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Personal Details for {self.wdId.empId}"


# Employee Insurance Details
class EmpInsuranceDetails(models.Model):
    isdId = models.AutoField(primary_key=True)
    wdId = models.ForeignKey(EmpWorkDetails, on_delete=models.CASCADE)
    fathersName = models.CharField(max_length=100, null=True, blank=True)
    fathersDOB = models.DateField(null=True, blank=True)
    mothersName = models.CharField(max_length=100, null=True, blank=True)
    mothersDOB = models.DateField(null=True, blank=True)
    spouseName = models.CharField(max_length=100, null=True, blank=True)
    spouseDOB = models.DateField(null=True, blank=True)
    child1 = models.CharField(max_length=100, null=True, blank=True)
    child1DOB = models.DateField(null=True, blank=True)
    child2 = models.CharField(max_length=100, null=True, blank=True)
    child2DOB = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Insurance Details for {self.wdId.empId}"

class EmpSalaryDetails(models.Model):
    sdId = models.AutoField(primary_key=True)  # Primary key for the salary details

    # Foreign Key to EmpWorkDetails
    wdId = models.ForeignKey(EmpWorkDetails, on_delete=models.CASCADE)

    # Salary components, reflecting the company's compensation structure
    CTCpayAMT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Cost to Company (CTC)
    BasicpayAMT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Basic pay
    HRApayAMT = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # House Rent Allowance (HRA)
    AdvancesAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Advances, if any
    VariableAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Variable pay
    QAllowanceAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Quarterly Allowance
    QBonusAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Quarterly Bonus
    ABonusAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Annual Bonus
    SAllowancesAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Special Allowances
    PTAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Professional Tax
    PFAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Provident Fund Amount (PF)
    ESIAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Employee State Insurance (ESI)
    DLoansAMT = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Deducted Loans, if any

    def __str__(self):
        return f"Salary Details for Employee: {self.wdId.empId}"