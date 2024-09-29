from django.db import models

class EmpWorkDetails(models.Model):
    wdId = models.AutoField(primary_key=True)
    empId = models.CharField(max_length=255, unique=True)
    employmentStatus = models.CharField(max_length=100)
    companyEmailId = models.EmailField()
    dateOfJoining = models.DateField()
    dateOfRelieving = models.DateField(null=True, blank=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    group = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100)
    roleType = models.CharField(max_length=100)
    currentRole = models.CharField(max_length=100)
    reportingManager = models.CharField(max_length=100)
    reasonForLeaving = models.TextField(null=True, blank=True)
    monthYearOfTermination = models.CharField(max_length=100, null=True, blank=True)
    totalExpInThisCompany = models.CharField(max_length=100, null=True, blank=True)
    totalExperience = models.CharField(max_length=100, null=True, blank=True)
    totalExpBeforeJoining = models.CharField(max_length=100, null=True, blank=True)
    previousDateOfJoining = models.DateField(null=True, blank=True)
    previousEmployer = models.CharField(max_length=100, null=True, blank=True)

class EmpSocialSecurityDetails(models.Model):
    ssdId = models.AutoField(primary_key=True)
    wdId = models.ForeignKey(EmpWorkDetails, on_delete=models.CASCADE)
    panNum = models.CharField(max_length=20)
    uanNum = models.CharField(max_length=20)
    aadharNum = models.CharField(max_length=20)
    bankName = models.CharField(max_length=100)
    ifscCode = models.CharField(max_length=20)
    bankAccountNumber = models.CharField(max_length=50)

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
