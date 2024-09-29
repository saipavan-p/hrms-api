from django.db import models

class Login(models.Model):
    id = models.AutoField(primary_key=True)  
    userName = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phoneNum = models.CharField(max_length=15)

    def __str__(self):
        return self.userName
