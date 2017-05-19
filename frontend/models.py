from django.db import models
from affiliate.models import *
from lica.model_meta import EnumField , STUDENTLEVEL
# Create your models here.


    
class Department(models.Model):
    departmentname = models.CharField(max_length=30,null=True,blank=True)       
    image = models.ImageField(upload_to='static_files/images/department')
    def __str__(self):
        return str(self.departmentname)
    
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
    aemail = models.EmailField(null=True , blank=True)
    firstname =models.CharField(max_length = 30,blank=True,verbose_name='First Name',null=True)
    middlename =models.CharField(max_length = 30,blank=True,verbose_name='Middle Name',null=True)
    lastname =models.CharField(max_length = 30,blank=True,verbose_name='Last Name',null=True)
    fk_college = models.ForeignKey(College,null=True)
    fk_campaign = models.ForeignKey(Campaign,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True,blank=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    mobile=models.CharField(max_length=20,null=True,blank=True)
    bonuspoints=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    verified=models.BooleanField(default=False)
    verifiedat=models.DateTimeField(null=True)
    level=EnumField(choices=STUDENTLEVEL)
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
    timestamp = models.DateTimeField(auto_now_add=True)
    fk_student =models.ForeignKey(Student)
    fk_intrest =models.ManyToManyField(Intrest,null=True,through='Question_Intrest')
    fk_department = models.ManyToManyField(Department,null=True,through='Question_Department')
    
class Hits(models.Model):
    fk_student=models.ForeignKey(Student)
    timestamp=models.DateTimeField(auto_now_add=True)
    fk_question=models.ForeignKey(Questions)

class Likes(models.Model):
    fk_student=models.ForeignKey(Student)
    timestamp=models.DateTimeField(auto_now_add=True)
    fk_question=models.ForeignKey(Questions)
    def __str__(self):
        return str(self.fk_student)
    
    
class Question_Intrest(models.Model):
    questions=models.ForeignKey(Questions)
    intrest=models.ForeignKey(Intrest)
    
class Question_Department(models.Model):
    questions=models.ForeignKey(Questions)
    department=models.ForeignKey(Department)
    
class Answers(models.Model):
    fk_questions = models.ForeignKey(Questions)
    answer =models.TextField()
    likes =models.IntegerField(default=0)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    
class Comment(models.Model):
    fk_answers = models.ForeignKey(Answers)
    comment =models.TextField()
    likes=models.IntegerField(default=0)
    
class Index_NewsFeed(models.Model):
    first=models.TextField()
    second=models.TextField()
    third=models.TextField()
    fourth=models.TextField()
    fifth=models.TextField()
    def __str__(self):
        return str(id)






    
