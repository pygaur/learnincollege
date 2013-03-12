from django.db import models

# Create your models here.

class College(models.Model):
    collegename = models.TextField()
    place = models.TextField(max_length = 30)
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zone=models.CharField(max_length=30)
    zipcode=models.IntegerField()
    new = models.IntegerField()

    
class Department(models.Model):
    departmentname = models.CharField(max_length=30,null=True,blank=True)       
    image = models.ImageField(upload_to='static_files/images/department')
    
class Intrest(models.Model):
    intrestfieldname = models.CharField(max_length=30)
    minimumage =models.IntegerField()
    maximumage = models.IntegerField()
    image = models.ImageField(upload_to='static_files/images/intrest')
    def __str__(self):
        return str(self.intrestfieldname)
    
    
    
class Student(models.Model):
    username = models.CharField(max_length = 30,blank=True,verbose_name='User Name',unique=True)
    password =models.CharField(max_length=128)
    dob = models.DateField(null=True,blank=True,verbose_name = "Date of Birth")
    age=models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True , blank=True)
    firstname =models.CharField(max_length = 30,blank=True,verbose_name='First Name',null=True)
    middlename =models.CharField(max_length = 30,blank=True,verbose_name='Middle Name',null=True)
    lastname =models.CharField(max_length = 30,blank=True,verbose_name='Last Name',null=True)
    fk_college = models.ForeignKey(College,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField(null=True,blank=True)
    def __str__(self):
        return str(self.username)
    
    
    
class Intrestinfo(models.Model):
    fk_student = models.ForeignKey(Student)
    fk_intrest =models.ForeignKey(Intrest)
    def __str__(self):
        return str(self.id)
    
class Departmentinfo(models.Model):
    fk_student = models.ForeignKey(Student)
    fk_department =models.ForeignKey(Department)
    
    
class Questions(models.Model):
    title = models.TextField()
    subject =models.TextField()
    hits = models.IntegerField()
    comment =models.IntegerField()
    likes =models.IntegerField()
    timestamp = models.DateTimeField()
    fk_student =models.ForeignKey(Student)
    fk_intrest =models.ForeignKey(Intrest)
    fk_department = models.ForeignKey(Department,null=True)
    
    
    
class Answers(models.Model):
    fk_questions = models.ForeignKey(Questions)
    likes =models.IntegerField()
    