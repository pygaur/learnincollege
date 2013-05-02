from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from frontend.models import *
from django.http import HttpRequest , HttpResponseRedirect
from frontend.function import *
from django.contrib.sites.models import get_current_site
from django.db.models import Q
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.auth.models import get_hexdigest

'''home page '''


#def get_hexdigest(algorithm, salt, raw_password):
#    """
#Returns a string of the hexdigest of the given plaintext password and salt
#using the given algorithm ('md5', 'sha1' or 'crypt').
#"""
#    raw_password, salt = smart_str(raw_password), smart_str(salt)
#    if algorithm == 'crypt':
#        try:
#            import crypt
#        except ImportError:
#            raise ValueError('"crypt" password algorithm not supported in this environment')
#        return crypt.crypt(raw_password, salt)
#
#    if algorithm == 'md5':
#        return md5_constructor(salt + raw_password).hexdigest()
#    elif algorithm == 'sha1':
#        return sha_constructor(salt + raw_password).hexdigest()
#    raise ValueError("Got unknown password algorithm type in password.")


def enc_password(password):
    import random
    algo = 'sha1'
    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
    hsh = get_hexdigest(algo, salt, password)
    password = '%s$%s$%s' % (algo, salt, hsh)
    return password


def index(request):
    
    sessionid = request.session.get('id') 
    try:
        obj = Student.objects.get(id=sessionid)
        return HttpResponseRedirect("/home/"+obj.username)
    except:
        pass
 
           
 
    return render_to_response('frontend/index.html',locals(),context_instance=RequestContext(request))



def seestudentlike(request , id):
    likesobj = Likes.objects.filter(fk_question__id=id)
    studentlist=[]
    for i in likesobj:
        studentlist.append(str(i.fk_student.username))
    
    studentlist=list(set(studentlist))
    return render_to_response('frontend/see-likes-students.html',locals(),context_instance=RequestContext(request))




def home(request , username):
    sessionid = request.session.get('id') 
    try:
        obj = Student.objects.get(id=sessionid)
    except:
        return HttpResponseRedirect('/')
    
    questionsobj = Questions.objects.all()
    totalhitlist=[]
    totallikelist=[]
    answerscount = []
    latestanswerlist=[]
    for i in questionsobj:
        totalhits=Hits.objects.filter(fk_question=i).count()
        totalhitlist.append(totalhits)
    
    for i in questionsobj:
        totallikes=Likes.objects.filter(fk_question=i).count()
        totallikelist.append(totallikes)
    
    for i in questionsobj:
        answers = Answers.objects.filter(fk_questions=i).count()
        answerscount.append(answers)
        latestanswer=Answers.objects.filter(fk_questions=i).order_by('-id')[:1]
        if not latestanswer:
            latestanswerlist.append("N.A.")
        else:
           for j in latestanswer:
                latestanswerlist.append(j.answer)
            
            
    print     
    questions = zip(questionsobj, totalhitlist ,totallikelist,latestanswerlist ,answerscount)
    
    
    return render_to_response('frontend/home.html',locals(),context_instance=RequestContext(request))



def submitlike(request ,id,student):
    message = {'result':''}
    if request.is_ajax():
        try:
            obj=Student.objects.get(username=student)
            questionobj = Questions.objects.get(id=id)
            likes=Likes.objects.get_or_create(fk_student=obj,fk_question=questionobj)
            message['result'] = 'True'
        except:
            message['result'] = 'False'
        
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')    
    



def submitunlike(request ,id,student):
    message = {'result':''}
    if request.is_ajax():
        try:
            print "Hiiiii"
            obj=Student.objects.get(username=student)
            print obj
            
            questionobj = Questions.objects.get(id=id)
            
            likes=Likes.objects.get(fk_student=obj,fk_question=questionobj)
            print likes
            likes.delete()
            message['result'] = 'True'
        except:
            message['result'] = 'False'
        
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')    
    



def questiondetails(request ,id):
    sessionid = request.session.get('id') 
    try:
        obj = Student.objects.get(id=sessionid)
    except:
        return HttpResponseRedirect('/')
    questionobj = Questions.objects.get(id=id)
    hitobj = Hits.objects.create(fk_question=questionobj,fk_student=obj)
    totalhits=Hits.objects.filter(fk_question=questionobj).count()
    totallikes=Likes.objects.filter(fk_question=questionobj).count()
    
    return render_to_response('frontend/question-details.html',locals(),context_instance=RequestContext(request))



def ask_question(request):
    sessionid = request.session.get('id') 
    try:
        obj = Student.objects.get(id=sessionid)
    except:
        return HttpResponseRedirect('/')
    
    if request.method == "GET":
        #intrestobj = Intrestinfo.objects.filter(fk_student=obj)
        intrestobj = Intrestinfo.objects.all()
        
        #departmentobj = Departmentinfo.objects.filter(fk_student=obj)
        departmentobj = Departmentinfo.objects.all()
        return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
    
    if request.method == "POST":
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        intrest = request.POST.getlist('intrest')
        department = request.POST.getlist('department')
        if title == "":
            response ="Please Enter Title"        
            intrestobj = Intrestinfo.objects.filter(fk_student=obj)
            departmentobj = Departmentinfo.objects.filter(fk_student=obj)
            return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
        if subject == "":
            response ="Please Enter Subject."        
            intrestobj = Intrestinfo.objects.filter(fk_student=obj)
            departmentobj = Departmentinfo.objects.filter(fk_student=obj)
            return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
        if not intrest:
            response ="Please Enter Intrest."        
            intrestobj = Intrestinfo.objects.filter(fk_student=obj)
            departmentobj = Departmentinfo.objects.filter(fk_student=obj)
            return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
        if not department:
            response ="Please Enter Department."        
            intrestobj = Intrestinfo.objects.filter(fk_student=obj)
            departmentobj = Departmentinfo.objects.filter(fk_student=obj)
            return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
        
        questionobj = Questions.objects.create(title=title,subject=subject,fk_student=obj)
        for i in intrest:
            intrestobj = Intrest.objects.get(intrestfieldname=str(i))
            Question_Intrest.objects.create(questions=questionobj,intrest=intrestobj)
        
        for i in department:
            departmentobj = Department.objects.get(departmentname=str(i))
            Question_Department.objects.create(questions=questionobj,department=departmentobj)
        
        
        
        return HttpResponseRedirect('/home/'+obj.username)




def submitanswer(request,id):
    if request.method == 'GET':
        return render_to_response('frontend/submit-answer.html',locals(),context_instance=RequestContext(request))
    
    if request.method == 'POST':
        answer=request.POST.get('answer')
        if answer == '':
            response = "Please Enter Message."
            return render_to_response('frontend/submit-answer.html',locals(),context_instance=RequestContext(request))
        
        questionobj=Questions.objects.get(id=int(id))
        Answers.objects.create(fk_questions=questionobj,answer=answer)
        
        
        string='done'        
        return render_to_response('frontend/submit-answer.html',locals(),context_instance=RequestContext(request))







def signin(request):
    if request.method == "GET":
        return HttpResponseRedirect('/')
    if request.method  == "POST":
        username=request.POST.get('id_username')
        password=request.POST.get('id_password')
        if username == "":
            return HttpResponse("User Name can not be empty")
        if password == "":
            return HttpResponse("Password can not be empty")
        try:
            obj=Student.objects.get(username=username)
        except:
            return HttpResponse("User does not exist.")
        
        dbpassword = obj.password
        '''hash function password hash function generation'''
        a = dbpassword.split('$')
        hashdb = str(a[2])
        salt = str(a[1])
        usrhash = get_hexdigest(a[0],a[1],password)
        if hashdb == usrhash:
            request.session['id'] = str(obj.id)
            return HttpResponseRedirect("/home/"+obj.username)
        else:
            return HttpResponse("Please enter correct password.")
        

def signupstep1(request):
    if request.method == "POST":
        Name = request.POST.get('username')
        password = str(request.POST.get('password'))
        password1 = str(request.POST.get('cpassword'))
        Email = request.POST.get('email')
        Dob = request.POST.get('dob')
        
        
        Dob=jstopython(str(Dob))
        age=ageverify(Dob)
        print age         
        password1=enc_password(password1)
        obj = Student.objects.create(age=age,username=Name,password=password1,email=Email,dob=Dob,ip=request.META['REMOTE_ADDR'])
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
        intrestinfoobj = Intrestinfo.objects.filter(fk_student=obj)
        
        intrestinfolist = []
        for i in intrestinfoobj:
            intrestinfolist.append(int(str(i.fk_intrest.id)))
        intrestobj = Intrest.objects.all()
        for j in  intrestinfolist:
            intrestobj = intrestobj.exclude(id=j)
        intrestobj = intrestobj.filter(Q(minimumage__lte=age) and Q(maximumage__gte=age))
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
    return HttpResponseRedirect(reverse('profile',args=(username,)))


def profile(request,username):
    id = request.session.get('id')
    try:
        obj=Student.objects.get(id=id)
        username = obj.username
    except:
        return HttpResponse('404 ERROR')
    intrests = Intrestinfo.objects.filter(fk_student=obj)
    departments = Departmentinfo.objects.filter(fk_student=obj)
    
    return render_to_response('frontend/student-profile.html',locals(),context_instance=RequestContext(request)) 

def logout(request):
    sessionid = request.session.get('id')
    try:
        del request.session['id']
    except:
        pass
    return HttpResponseRedirect('/')
   

def checkuseravailability(request,username):
    message = {'result':''}
    if request.is_ajax():
        try:
            obj = Student.objects.get(username=username)
            message['result'] = 'True'
        except:
            message['result'] = 'False'
        
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')    
    
    
    
    

    
    
    
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
    
    
    
    
    