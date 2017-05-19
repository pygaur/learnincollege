# Create your views here.
import time

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse ,HttpResponseRedirect
from django.core.validators import validate_email
try:
    from django.contrib.sites.models import get_current_site
except ImportError:
    from django.contrib.sites.shortcuts import get_current_site

from affiliate.models import *


def is_valid_email(email):
    if validate_email(email):
        return True
    return False


def home(request):
    ''' home page for affiliates'''
    return render_to_response("affiliate/index.html",locals(),context_instance=RequestContext(request))

def signupvalidation(request,name,password,password1,state,country,email,mobile):
    if name == "":
        response="Name can not be empty"
        return response
    if password == "":
        response="Password can not be empty"
        return response
    if password1 == "":
        response = "Repeat Password can not be empty"
        return response
    if state == "":
        response=="State is required"
        return response
   
    if country == "":
        response ="Country can not be empty"
        return response
    if email == "":
        response = "Email can not be empty"
        return response
    if mobile == "":
        response = "Mobile can not be empty"
        return response
    
    mailvalidation=is_valid_email(email)
    if mailvalidation == False:
        response = "Enter Valid Email address"
        return response
    try:
        mobile=int(mobile)
    except:
        response="Enter Valid Mobile"
        return response
        
    if password != password1:
        response="Password must  be matching"
        return response

def signup(request):
    '''sign up for colleges
    in post method we will register new entries 
    '''
    
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        state=request.POST.get('state')
        country=request.POST.get('country')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        
        '''validation checking on server'''
        
        response = signupvalidation(request ,name,password,password1,state,country,email,mobile)
        if response != None:
            return render_to_response("affiliate/index.html",locals(),context_instance=RequestContext(request))
    
        
        
        collegeobj = College.objects.create(name=name,state=state,country=country,password=password1 ,email=email,mobile=mobile,ip=request.META['REMOTE_ADDR'])
        collegeobj.code = int(time.time())
        collegeobj.save()
        request.session['affid'] = str(collegeobj.id)
        return HttpResponseRedirect("/profile-college/")
    
    if request.method == "GET":
        return HttpResponseRedirect('/affiliate/')
        



def signin(request):
    if request.method == "POST":
        code=request.POST.get('code')
        password=request.POST.get('password')
        
        try:
            collegeobj=College.objects.get(code=code)
        except:
            response="College not found"
            return render_to_response("affiliate/index.html",locals(),context_instance=RequestContext(request))
        
        
        Password=collegeobj.password
        
        if password == Password:
            request.session['affid'] = str(collegeobj.id)
            return HttpResponseRedirect(reverse('affiliate-profile'))
    
            
    if request.method == "GET":
        return HttpResponseRedirect('/affiliate/')
        
    
        
def profile(request):
    sessionid = request.session.get('affid') 
    try:
        collegeobj = College.objects.get(id=sessionid)
    except:
        return HttpResponse("404")
    if request.method == "GET":
        return render_to_response("affiliate/profile.html",locals(),context_instance=RequestContext(request))

def editprofile(request):
    sessionid = request.session.get('affid') 
    try:
        collegeobj = College.objects.get(id=sessionid)
    except:
        return HttpResponse("404")
    if request.method == "GET":
        
        collegeacademicobj=CollegeAcademic.objects.get_or_create(fk_college=collegeobj)[0]
        return render_to_response("affiliate/edit-profile.html",locals(),context_instance=RequestContext(request))
    if request.method == "POST":
        
        name=str(request.POST.get("name"))
        place=str(request.POST.get("place"))
        country=str(request.POST.get("country"))
        state=str(request.POST.get("state"))
        zone=str(request.POST.get("zone"))
        zipcode=str(request.POST.get("zipcode"))
        university=str(request.POST.get("university"))
        email=str(request.POST.get("email"))
        aemail=str(request.POST.get("aemail"))
        mobile=str(request.POST.get("mobile"))
        phone=str(request.POST.get("phone"))
        
        if name == "":
            response ="Please enter Name"
        if place == "":
            response ="Please enter Place"
        if country == "":
            response ="Please enter Country"
        if state == "":
            response ="Please enter state"
        if zone == "":
            response ="Please enter Zone"
        if zipcode == "None":
            response ="Please enter Zip Code"
        if university == "":
            response ="Please enter University"
        if email == "":
            response ="Please enter Email Address"
        if mobile == "":
            response ="Please enter Mobile Number"
            
        
        
        collegeobj.name=name
        collegeobj.place=place
        collegeobj.country=country
        collegeobj.state=state
        collegeobj.zone=zone
        collegeobj.zipcode=zipcode
        collegeobj.university=university
        collegeobj.email=email
        collegeobj.aemail=aemail
        collegeobj.mobile=mobile
        collegeobj.phone=phone
        collegeobj.save()
        return render_to_response("affiliate/edit-profile.html",locals(),context_instance=RequestContext(request))
        
        
def editprofileextra(request):
    sessionid = request.session.get('affid') 
    try:
        collegeobj = College.objects.get(id=sessionid)
    except:
        return HttpResponse("404")
    if request.method == "GET":
        return HttpResponseRedirect('/affiliate/')    
    if request.method == "POST":
        
        strength=str(request.POST.get("strength"))
        director=str(request.POST.get("director"))
        stablished=request.POST.get("stablished")
        print stablished
        if strength == "":
            response ="Please enter Strength."
        if director == "":
            response ="Please enter Director"
        if stablished == "":
            response ="Please enter Stablished"
        
        collegeacademicobj=CollegeAcademic.objects.get_or_create(fk_college=collegeobj)[0]
        collegeacademicobj.strength=strength
        collegeacademicobj.director=director
        collegeacademicobj.stablished=stablished
        collegeacademicobj.save()
        return HttpResponseRedirect('/edit-profile-college/')    

        
        
        
        
        
        
        
        
def logout(request):
    return HttpResponse("LOGOUT")
        
def passwordchange(request):
    return HttpResponse(" password change ")


def passwordreset(request):
    return HttpResponse("password reset")
        
        
def campaign(request):
    sessionid = request.session.get('affid') 
    try:
        collegeobj = College.objects.get(id=sessionid)
    except:
        return HttpResponse("404")
    if request.method == "GET":
        links = Campaign.objects.filter(fk_college = collegeobj).order_by('-id')
        return render_to_response("affiliate/campaign.html",locals(),context_instance=RequestContext(request))
    
    if request.method == "POST":
        linkname=request.POST.get('name')
        currentsite = get_current_site(request)
        currentsite = str(currentsite.domain)
    
        
        try:
            linkobj = Campaign.objects.create(fk_college=collegeobj,name=linkname)
        except:
            return HttpResponse("LInk name is unique")
        try:
            linkurl = 'http://'+currentsite+'/'+linkname
        except:
            print sys.exc_info()
        
        linkobj.link = linkurl
        linkobj.name = linkname
        linkobj.save()
        
            
        promotion = 'link'
        links = Campaign.objects.filter(fk_college = collegeobj).order_by('-id')
        return render_to_response("affiliate/campaign.html",locals(),context_instance=RequestContext(request))
        
        
        
        
        
        
        
        
        
        
        
