from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100,null=True,unique=True)
    password=models.CharField(max_length=128)
    place = models.CharField(max_length = 30,null=True)
    country=models.CharField(max_length=30,null=True)
    state=models.CharField(max_length=30,null=True)
    zone=models.CharField(max_length=30,null=True)
    zipcode=models.IntegerField(null=True)
    registrationat=models.DateTimeField(auto_now_add=True,null=True)
    ip=models.IPAddressField(null=True)
    university=models.CharField(null=True,max_length=100)
    address=models.TextField(null=True)
    email=models.EmailField(null=True)
    aemail=models.EmailField(null=True)
    mobile=models.CharField(max_length=15,null=True)
    phone=models.CharField(max_length=15,null=True)
    code=models.CharField(max_length=10,unique=True,null=True)
    
class CollegeAcademic(models.Model):
    fk_college=models.OneToOneField(College)
    strength=models.CharField(null=True,max_length=50)
    director=models.CharField(max_length=50,null=True)
    stablished=models.DateField(null=True)
    
    
    
class Campaign(models.Model):
    fk_college=models.ForeignKey(College)
    name=models.CharField(max_length=20,unique=True)
    link=models.TextField()
    