from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from frontend.models import *
from django.http import HttpRequest , HttpResponseRedirect
from frontend.function import *
from django.contrib.sites.models import get_current_site
from django.db.models import Q
'''home page '''


def get_hexdigest(algorithm, salt, raw_password):
    """
Returns a string of the hexdigest of the given plaintext password and salt
using the given algorithm ('md5', 'sha1' or 'crypt').
"""
    raw_password, salt = smart_str(raw_password), smart_str(salt)
    if algorithm == 'crypt':
        try:
            import crypt
        except ImportError:
            raise ValueError('"crypt" password algorithm not supported in this environment')
        return crypt.crypt(raw_password, salt)

    if algorithm == 'md5':
        return md5_constructor(salt + raw_password).hexdigest()
    elif algorithm == 'sha1':
        return sha_constructor(salt + raw_password).hexdigest()
    raise ValueError("Got unknown password algorithm type in password.")


def home(request):
    return render_to_response('frontend/index.html',locals(),context_instance=RequestContext(request))

def signupstep1(request):
    if request.method == "POST":
        Name = request.POST.get('username')
        password = str(request.POST.get('password'))
        password1 = str(request.POST.get('cpassword'))
        Email = request.POST.get('email')
        Dob = request.POST.get('dob')
        age=ageverify(Dob)
        obj = Student.objects.create(age=age,username=Name,password=password1,email=Email,dob=Dob)
        username =str(obj.username)
        request.session['id'] = str(obj.id)
        return HttpResponseRedirect(reverse('signupstep2'))
    
    if request.method == 'GET':
        return render_to_response('frontend/index.html',locals(),context_instance=RequestContext(request))


def signupstep2(request):
    id = request.session.get('id')
    try:
        obj=Student.objects.get(id=id)
    except:
        return HttpResponse('404 ERROR')
    if request.method == "GET":
        age = obj.age
        print obj ,age
        intrestinfoobj = Intrestinfo.objects.filter(fk_student=obj)
        
        print intrestinfoobj ,'prashant'
        intrestinfolist = []
        for i in intrestinfoobj:
            intrestinfolist.append(int(str(i.fk_intrest.id)))
        intrestobj = Intrest.objects.all()
        for j in  intrestinfolist:
            intrestobj = intrestobj.exclude(id=j)
        intrestobj = intrestobj.filter(Q(minimumage__lte=age) and Q(maximumage__gte=age))
        print intrestobj ,'ssssssssssss'
        currentsite = str(get_current_site(request).domain)
        return render_to_response('frontend/signup-step2.html',locals(),context_instance=RequestContext(request))
    
def signupstep22(request,intrestid):
    id = request.session.get('id')
    try:
        obj=Student.objects.get(id=id)
    except:
        return HttpResponse('404 ERROR')
    intrestobj = Intrest.objects.get(id=intrestid)
    Intrestinfo.objects.get_or_create(fk_student=obj,fk_intrest=intrestobj)
    return HttpResponseRedirect(reverse('signupstep2'))
    
def signupstep3(request):
    id = request.session.get('id')
    try:
        obj=Student.objects.get(id=id)
    except:
        return HttpResponse('404 ERROR')
    if request.method == "GET":
        departmentobj = Department.objects.all()
        currentsite = str(get_current_site(request).domain)
        return render_to_response('frontend/signup-step3.html',locals(),context_instance=RequestContext(request))
    
def signupstep32(request,departmentid):
    id = request.session.get('id')
    try:
        obj=Student.objects.get(id=id)
        username = obj.username
    except:
        return HttpResponse('404 ERROR')
    departmentobj = Department.objects.get(id=departmentid)
    Departmentinfo.objects.get_or_create(fk_student=obj,fk_department=departmentobj)
    return HttpResponseRedirect(reverse('welcome',args=(username,)))
import json   

def checkuseravailability(request,username):
    respose = {'result':''}
    if request.is_ajax():
        try:
            obj = Student.objects.get(username=username)
            response['result'] = 'True'
        except:
            response['result'] = 'False'
        data=json.dumps(response)
        return HttpResponse(data ,mimetype="application/json")

    
    
    

    
    
    
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import load_backend, login
from django.contrib.auth.models import User
from django.shortcuts import redirect


def user_login(request, user_id):
    if not request.user.is_superuser:
        messages.error(request, "You need to be a superuser to do that.")
        return redirect(request.META.get("HTTP_REFERER", "/"))

    user = User.objects.get(pk=user_id)

    # Find a suitable backend.
    if not hasattr(user, 'backend'):
        for backend in settings.AUTHENTICATION_BACKENDS:
            if user == load_backend(backend).get_user(user.pk):
                user.backend = backend
                break

    # Log the user in.
    if hasattr(user, 'backend'):
        login(request, user)

    return redirect("/")    
    
    
    
    
    
