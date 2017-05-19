from model_meta import *
from frontend.models import *
from affiliate.models import *
from lica.signals import onlogin
from django.db.models.signals import pre_save ,post_save , post_delete ,pre_delete



class Messagesettings(models.Model):
    subject=models.CharField(max_length=500,blank=True)
    message=models.TextField(blank=True)
    active=models.BooleanField(default=True)
    
    
class Messagetriggers(models.Model):
    triggername=EnumField(choices=TRIGGERS)
    fk_messagesettings=models.ForeignKey(Messagesettings)
    active=models.BooleanField(default=True)
    
    
class Bonussetting(models.Model):
    bonusname =models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    credittype=EnumField(choices=CREDITTYPE)
    message=models.CharField(max_length=100)
    product=models.CharField(default="LEARNINCOLLEGE",max_length=20)
    validfrom=models.DateTimeField()
    validto=models.DateTimeField()
    validtimes = models.BooleanField(default=False)
    validtimesvalue=models.IntegerField(null=True)
    validdays=models.IntegerField(null=True,blank=True)
    offerdays=models.IntegerField(null=True,blank=True)
    currency=models.CharField(max_length=3)
    amount=models.IntegerField(null=True)
    chunks =models.BooleanField(default=False)
    chunksvalue=models.IntegerField(default=0)
    active=models.BooleanField(default=True)


class Bonustrigger(models.Model):
    fk_bonussetting=models.ForeignKey(Bonussetting)
    type=EnumField(choices=BONUSTRIGGERTYPE)
    validfrom=models.DateTimeField()
    validto=models.DateTimeField()
    level=models.IntegerField(null=True)
    fk_college=models.ForeignKey(College)
    active=models.BooleanField(default=True)




class Loginlogs(models.Model):
    """
    This model will be used to calculate login activity
    of students
    """
    fk_student=models.ForeignKey(Student)
    timestamp=models.DateTimeField(auto_now_add=True)
    loginip=models.GenericIPAddressField()
    loginok=models.BooleanField(default=False)
    uniquelogin=models.BooleanField(default=False)

post_save.connect(onlogin,sender=Loginlogs)       


class Emailverificationlogs(models.Model):
    """
    this model is for email verification link
    to check unique token + single time usable
    + time expire
    """
    fk_student = models.ForeignKey(Student)
    token = models.CharField(max_length=20)

class PasswordResetlogs(models.Model):
    """
    this model is for password reset when any player will submit
    password reset here one entry will be craeted and when reset
    will be done entry will be deleted.
    """
    fk_student= models.ForeignKey(Student)
    token = models.CharField(max_length=10)
    expiretimestamp=models.DateTimeField()
    
    
    



    
