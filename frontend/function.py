import random
from datetime import datetime ,  date
from lica.models import *
from django.core.mail import EmailMessage
from django.template import Context , Template
import time
import string
from random import choice
from django.core.validators import validate_email


def ageverify(Birthday):
    tyear = datetime.now().year
    tmonth = datetime.now().month
    tdate = datetime.now().date
    days = 365.25
    from datetime import date
    age = int((date.today() - Birthday).days/days)
    return age

def jstopython(Dob):
    month = str(Dob.split('/')[0])
    date = str(Dob.split('/')[1])
    year= str(Dob.split('/')[2])
    a = int(year)
    b =int(month)
    c= int(date)
    from datetime import date
    Dob= date(a,b,c)
    return Dob

def is_valid_email(email):
    if validate_email(email):
        return True
    return False
    

class GeneralFunctions:
    def Genkey(self,length=10, chars=string.letters + string.digits):
        string = ''.join([choice(chars) for i in range(length)])
        referenceno = string + str(int(time.time()))
        return referenceno


    
    
class MailSending:
    def __init__(self, obj, trigger):
        self.obj = obj
        self.trigger = trigger

    def loginmail(self):
        messagetrigger = Messagetriggers.objects.filter(triggername = self.trigger)
        for i in messagetrigger:
            if i.active == True:
                templateid =   str(i.fk_messagesettings_id)
                messagetemplateobject = Messagesettings.objects.get(id = templateid)
                subject =  messagetemplateobject.subject
                content =  messagetemplateobject.message
                a =Template(content)
                b = Context(locals())
                d = a.render(b)
                msg = EmailMessage(subject,d,"""LearninCollege <mail@learnincollege>""",[self.obj.email],headers = {'CC': '91prashantgaur@gmail.com'})
                msg.content_subtype="html"
                msg.send()

    def signupmail(self ,password):
        messagetrigger = Messagetriggers.objects.filter(triggername = self.trigger)
        for i in messagetrigger:
            if i.active == True:
                templateid =   str(i.fk_messagesettings_id)
                messagetemplateobject = Messagesettings.objects.get(id = templateid)
                subject =  messagetemplateobject.subject
                content =  messagetemplateobject.message
                a =Template(content)
                b = Context(locals())
                d = a.render(b)
                msg = EmailMessage(subject,d,"""LearninCollege <mail@learnincollege>""",[self.obj.email],headers = {'CC': '91prashantgaur@gmail.com'})
                msg.content_subtype="html"
                msg.send()

    def emailverificationmail(self ,result):
        messagetrigger = Messagetriggers.objects.filter(triggername = self.trigger)
        for i in messagetrigger:
            if i.active == True:
                templateid =   str(i.fk_messagesettings_id)
                messagetemplateobject = Messagesettings.objects.get(id = templateid)
                subject =  messagetemplateobject.subject
                content =  messagetemplateobject.message
                a =Template(content)
                obj=result[0]
                token=result[1]
                b = Context(locals())
                d = a.render(b)
                msg = EmailMessage(subject,d,"""LearninCollege <mail@learnincollege>""",[self.obj.email],headers = {'CC': '91prashantgaur@gmail.com'})
                msg.content_subtype="html"
                msg.send()

    def emailverificationmail(self ,tokenobj):
        messagetrigger = Messagetriggers.objects.filter(triggername = self.trigger)
        for i in messagetrigger:
            if i.active == True:
                templateid =   str(i.fk_messagesettings_id)
                messagetemplateobject = Messagesettings.objects.get(id = templateid)
                subject =  messagetemplateobject.subject
                content =  messagetemplateobject.message
                a =Template(content)
                studentname=tokenobj.fk_student
                token=tokenobj.token
                expireid=tokenobj.id
                
                print studentname ,token ,expireid
                b = Context(locals())
                d = a.render(b)
                msg = EmailMessage(subject,d,"""LearninCollege <mail@learnincollege>""",[self.obj.email],headers = {'CC': '91prashantgaur@gmail.com'})
                msg.content_subtype="html"
                msg.send()

