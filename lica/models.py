from model_meta import *
from frontend.models import *
from affiliate.models import *

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
    bonussplit=models.IntegerField(default=0)
    multiplication=models.IntegerField(default=0)
    active=models.BooleanField(default=True)


class Bonustrigger(models.Model):
    fk_bonussetting=models.ForeignKey(Bonussetting)
    type=EnumField(choices=BONUSTRIGGERTYPE)
    validfrom=models.DateTimeField()
    validto=models.DateTimeField()
    level=models.IntegerField(null=True)
    fk_college=models.ForeignKey(College)
    active=models.BooleanField(default=True)








    