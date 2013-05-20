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
from django.core.urlresolvers import resolve
from  django.core.paginator import Paginator , InvalidPage , EmptyPage
from django.views.generic.base import TemplateView
import re
from datetime import datetime , timedelta
'''home page '''




def enc_password(password):
    """"
    this function is responsible to generate
    hash code of any string
    """
    
    import random
    algo = 'sha1'
    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
    hsh = get_hexdigest(algo, salt, password)
    password = '%s$%s$%s' % (algo, salt, hsh)
    return password


def index(request):
    
    
    """
    index page ,
    entry page of our website
    """
    """ fetching session to check student is already login or not """
    sessionid = request.session.get('id') 
    try:
        obj = Student.objects.get(id=sessionid)
        """
        it will redirect to home by default if player is already login
        into system
        """
        return HttpResponseRedirect("/home/"+obj.username)
    except:
        pass
    try:
        newsfeed=list(Index_NewsFeed.objects.all())[-1]
    except:
        pass
    return render_to_response('frontend/index.html',locals(),context_instance=RequestContext(request))



def seestudentlike(request , id):
    """
    this function will return
    students name who like any question
    we will pass question id
    seestudentlike(requst ,1)
    """
    
    """
    question is foreign key to likes table
    """
    likesobj = Likes.objects.filter(fk_question__id=id)
    studentlist=[]
    for i in likesobj:
        studentlist.append(str(i.fk_student.username))
    
    studentlist=list(set(studentlist))
    return render_to_response('frontend/see-likes-students.html',locals(),context_instance=RequestContext(request))




def home(request , username):
    """
    home page of student after login into system ,
    we will also pass username,
    
    home(request, prashantgaur)
    """
    sessionid = request.session.get('id') 
    try:
        obj = Student.objects.get(id=sessionid)
    except:
        return HttpResponseRedirect('/')
    
    
    
    
    
    
    # list of all questions
    questionsobj = Questions.objects.all()
    
    
    
    print questionsobj
    for i in questionsobj:
        print i.fk_student
    
    
    
    
    
    
    

    
    
    
    
    # list of tatal views of questions
    totalhitlist = []
    #list of total likes
    totallikelist = []
    #count of answers respect to each questions
    answerscount = []
    #this list will return latest answer of eash question
    latestanswerlist=[]                    
    #active player is already liked any question or not.
    likedone = []                            
    for i in questionsobj:
        
        likes=Likes.objects.filter(fk_student=obj,fk_question=i)
        if likes:
            likedone.append("YES")
        else:
            likedone.append("NO")
        
        
        totalhits=Hits.objects.filter(fk_question=i).count()
        totalhitlist.append(totalhits)
    
    for i in questionsobj:
        totallikes=Likes.objects.filter(fk_question=i).count()
        totallikelist.append(totallikes)
    
    for i in questionsobj:
        answers = Answers.objects.filter(fk_questions=i).count()
        answerscount.append(answers)
        #it will give latest answer of any question
        latestanswer=Answers.objects.filter(fk_questions=i).order_by('-id')[:1]
        if not latestanswer:
            latestanswerlist.append("N.A.")
        else:
           for j in latestanswer:
                latestanswerlist.append(j.answer)
                    
    questions = zip(questionsobj, totalhitlist ,totallikelist,latestanswerlist ,answerscount,likedone)
    
    
    
    
    paginator = Paginator(questions, 1)
    
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    
    try:
        questions = paginator.page(page)
    except (InvalidPage, EmptyPage):
        questions = paginator.page(paginator.num_pages)

    
    
    """
    code to display student's department
    and intrest
    now as requirement student can select many intrest
    and 1 department
    """
    
    
    try:
        department=Departmentinfo.objects.get(fk_student=obj)
    except:
        department =None
    intrest=Intrestinfo.objects.filter(fk_student=obj)    
    
    
    return render_to_response('frontend/home.html',locals(),context_instance=RequestContext(request))



def submitlike(request ,id,student):
    """
    ajax request
    it will accept request of any student
    to like any question .
    submitlike(request , 1, prashant).
    response is returned into json .
    """
    
    message = {'result':'','already':''}
    if request.is_ajax():
        try:
            obj=Student.objects.get(username=student)
            questionobj = Questions.objects.get(id=id)
            likes=Likes.objects.get_or_create(fk_student=obj,fk_question=questionobj)
            
            
            message['result'] = 'True'
            message['already'] = str(likes[1])
            
        except:
            message['result'] = 'False'
        
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')    
    



def submitunlike(request ,id,student):
    
    """
    ajax request
    it will accept request of any student
    to dis like any question .
    submitunlike(request , 1, prashant).
    response is returned into json .
    """
    
    message = {'result':''}
    if request.is_ajax():
        try:
            obj=Student.objects.get(username=student)
            questionobj = Questions.objects.get(id=id)
            
            likes=Likes.objects.get(fk_student=obj,fk_question=questionobj)
            likes.delete()
            message['result'] = 'True'
        except:
            message['result'] = 'False'
        
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')    
    



def questiondetails(request ,id):
    """
    this function will give details of any questin
    questiondetails(request ,1)
    count of Likes
    count of Views
    """
    
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
    """
    when player will submit any question
    Now he can bind department ,intrest
    to any question from all department ,intrest
    
    GET : return template with all department and intrest
    POST : submit  title , subject ,intrest ,department 
    """
    
    try:
        lasturl = request.META['HTTP_REFERER'].split('/')[3]
    
        if lasturl == "":
            return render_to_response("frontend/html/login.html",context_instance=RequestContext(request))
    except:
        pass
    sessionid = request.session.get('id') 
    try:
        obj = Student.objects.get(id=sessionid)
    except:
        return HttpResponseRedirect('/')
    
    if request.method == "GET":
        #intrestobj = Intrestinfo.objects.filter(fk_student=obj)
        #departmentobj = Departmentinfo.objects.filter(fk_student=obj)
        
        intrestobj = Intrest.objects.all()
        departmentobj = Department.objects.all()
        return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
    
    if request.method == "POST":
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        intrest = request.POST.getlist('intrest')
        department = request.POST.getlist('department')
        if title == "":
            response ="Please Enter Title"        
            
            #intrestobj = Intrestinfo.objects.filter(fk_student=obj)
            #departmentobj = Departmentinfo.objects.filter(fk_student=obj)
            intrestobj = Intrest.objects.all()
            departmentobj = Department.objects.all()
        
            return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
        if subject == "":
            response ="Please Enter Subject."        
            #intrestobj = Intrestinfo.objects.filter(fk_student=obj)
            #departmentobj = Departmentinfo.objects.filter(fk_student=obj)
            #
            intrestobj = Intrest.objects.all()
            departmentobj = Department.objects.all()
        
            return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
        if not intrest:
            response ="Please Enter Intrest."        
            intrestobj = Intrest.objects.all()
            departmentobj = Department.objects.all()
        
            
            return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
        if not department:
            response ="Please Enter Department."        
            intrestobj = Intrest.objects.all()
            departmentobj = Department.objects.all()
        
            return render_to_response('frontend/ask-question.html',locals(),context_instance=RequestContext(request))
        
        #for i in range(1,5000):
        questionobj = Questions.objects.create(title=title,subject=subject,fk_student=obj)
        
        
        
        for i in intrest:
            intrestobj = Intrest.objects.get(intrestfieldname=str(i))
            Question_Intrest.objects.create(questions=questionobj,intrest=intrestobj)
        
        for i in department:
            departmentobj = Department.objects.get(departmentname=str(i))
            Question_Department.objects.create(questions=questionobj,department=departmentobj)
        
        
        
        return HttpResponseRedirect('/home/'+obj.username)




def submitanswer(request,id):
    """
    when student will submit
    answer to any question .
    after submit answer
    i am sending string which will reload parent template
    and close that pop up page.
    
    """
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
    """
    signin(request)
    function responbile for login of
    player in website .
    """
    if request.method == "GET":
        #if player will hit signin url directly through browser
        return HttpResponseRedirect('/')
    
    if request.method  == "POST":
        username=request.POST.get('id_username')
        password=request.POST.get('id_password')
        
        if username == "":
            login_response = "Please Enter Your  Username."
            return render_to_response("frontend/index.html",locals(),context_instance=RequestContext(request))
        
        if password == "":
            login_response = "Please Enter Your  Password."
            return render_to_response("frontend/index.html",locals(),context_instance=RequestContext(request))
        
        try:
            obj=Student.objects.get(username=username)
            loginlogs=Loginlogs.objects.create(fk_student=obj,loginip=request.META["REMOTE_ADDR"])
        except:
            login_response = "Username is not registered with use."
            return render_to_response("frontend/index.html",locals(),context_instance=RequestContext(request))
        
        dbpassword = obj.password
        '''hash function password hash function generation'''
        a = dbpassword.split('$')
        hashdb = str(a[2])
        salt = str(a[1])
        usrhash = get_hexdigest(a[0],a[1],password)
        
        
        if hashdb == usrhash:
            #activating the session  
            request.session['id'] = str(obj.id)
            
            """function to send login mail"""
            try:
                trigger = "LOGIN"
                mail= MailSending(obj,trigger)
                mail.loginmail()
            except:
                pass
            
            loginlogs.loginok = True
            loginlogs.save()
            return HttpResponseRedirect("/home/"+obj.username)
        else:
            login_response = "Please enter corrent password."
            return render_to_response("frontend/index.html",locals(),context_instance=RequestContext(request))
        
        


class SignupStep1(TemplateView):
    def get(self,request):
        return render_to_response('frontend/index.html',locals(),context_instance=RequestContext(request))
    
    
    
    def emailverification(self,obj):
        function=GeneralFunctions()
        key = function.Genkey(length=10, chars=string.letters + string.digits)
        Emailverificationlogs.objects.create(fk_student=obj,token="ABCD",)
        verificationvariants=[]
        verificationvariants.append(obj)
        verificationvariants.append(key)
        return verificationvariants
    
    #def signupvalidation(Name, password, password1, Email, Dob):
    #    
    #    if Name == "":
    #        result = "Username can not be Empty."
    #        return result
    #    
    #    if password == "" or password1 == "":
    #        result = "Password can not be Empty."
    #        return result
    #    
    #    if Email == "":
    #        result = "Email address can not be empty."
    #        
    #    if password != password1:
    #        result = "Password does not matching."
    #        
    #    
    #    mailvalidation = is_valid_email(Email)
    #    
    #    if mailvalidation == False:
    #        response = "Please enter a valid Email Address."
    #        return response
    #    
    #    
    #    mailavailablity = Student.objects.filter(email=Email).exists()
    #    if mailavailablity == True:
    #        result = "Email is already registered with us."
    #        return result
    #    
    #    usernameavailablity = Student.objects.filter(username=Name).exists()
    #    if usernameavailablity == True:
    #        result = "Username is already registered with us."
    #        return result
    #    
    #    reg = re.compile('^[a-z0-9._A-Z]+$')
    #    reg = bool(reg.match(Name))
    #    if reg == False:
    #        response = "Only Alphabets, numbers, . And _ are allowed. Special Characters are not allowed. Please check."
    #        return response
    #    
    #    if (len(Name) < 4) or (len(Name) > 15):
    #        response = "A User Name can be of 4-15 characters only."
    #        return response
    #    
    #    if (len(password) < 4) or (len(password) > 15):
    #        response = "A password should have a minimum of 4 characters and maximum of 15 characters."
    #        return response
    #
    #    
        
        
        
        
        
    def post(self,request):
        Name = request.POST.get('username')
        password = str(request.POST.get('password'))
        password1 = str(request.POST.get('cpassword'))
        Email = request.POST.get('email')
        Dob = request.POST.get('dob')
        Dob=jstopython(str(Dob))
        
        #result = self.signupvalidation(Name, password, password1, Email, Dob)
        
        age=ageverify(Dob)
        password1=enc_password(password1)
        
        
        
        
        obj = Student.objects.create(age=age,username=Name,password=password1,email=Email,dob=Dob,ip=request.META['REMOTE_ADDR'],level="ZERO")
        username =str(obj.username)
        request.session['id'] = str(obj.id)
        
        trigger = "SIGNUP"
        mail= MailSending(obj,trigger)
        mail.signupmail(password)
        
        
        result = self.emailverification(obj)
        
        
        trigger = "VERIFICATION"
        mail= MailSending(obj,trigger)
        mail.emailverificationmail(result)
        
        #obj.delete()
        return HttpResponseRedirect(reverse('signupstep2'))
    




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
        current_url = resolve(request.path_info).url_name
        request.session['current_url'] = str(current_url)
        
        return render_to_response('frontend/signup-step2.html',locals(),context_instance=RequestContext(request))
    
def signupstep22(request,intrestid):
    id = request.session.get('id')
    try:
        obj=Student.objects.get(id=id)
        username = obj.username
    except:
        return HttpResponse('404 ERROR')
    intrestobj = Intrest.objects.get(id=intrestid)
    Intrestinfo.objects.get_or_create(fk_student=obj,fk_intrest=intrestobj)
    
    
    url = request.session.get('current_url')
    if url == "addintrest":
        try:
            del request.session['current_url']
        except:
            pass
        return HttpResponseRedirect(reverse('home',args=(username,)))
    
    
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
        
        currentsite = str(get_current_site(request).domain)
        current_url = resolve(request.path_info).url_name
        request.session['current_url'] = str(current_url)
           
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
    
    url = request.session.get('current_url')
    if url == "adddepartment":
        try:
            del request.session['current_url']
        except:
            pass
        return HttpResponseRedirect(reverse('home',args=(username,)))
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
    """
    delete  student session
    
    """
    
    sessionid = request.session.get('id')
    try:
        del request.session['id']
    except:
        pass
    return HttpResponseRedirect('/')
   

def checkuseravailability(request,username):
    """
    
    Ajax request to check
    user name availability
    
    return type is
    Ex :message{"result":'True'}
    
    Ajax code:
    
    
    $(document).ready(function () {
        $("#username").blur(mail_check)
                        });


    function mail_check() {
            var username = $("#email").val();
            $.getJSON('/checkusernameavailability/'+username+"/",
                
            function(data) {
            
            result = data.result
            if (result == "True"){
            
            CONDITIONS:(User name is already in db)
            
            }
            if (result == "False"){
            CONDITIONS:(user name is open to register)
        }});}

    """
    message = {'result':''}
    if request.is_ajax():
        try:
            obj = Student.objects.get(username=username)
            message['result'] = 'True'
        except:
            message['result'] = 'False'
        
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')    
    
def checkemailavailability(request,email):
    """
    Ajax request to check
    email availability
    
    return type is
    Ex :message{"result":'True'}
    
    Ajax code:
    
    
    $(document).ready(function () {
        $("#email").blur(mail_check)
                        });


    function mail_check() {
            var email = $("#email").val();
            $.getJSON('/checkemailavailability/'+email+"/",
                
            function(data) {
            
            result = data.result
            if (result == "True"){
            
            CONDITIONS:(Email id is already in db)
            
            }
            if (result == "False"){
            CONDITIONS:(Email id is open to register)
        }});}

    """
    
    
    message = {'result':''}
    if request.is_ajax():
        print 'ajax recieved'
        obj = Student.objects.filter(email=email)
        print len(obj)
        if len(obj) > 0:
            message['result'] = 'True'
        else:
            message['result'] = 'False'
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')    
    
    
    

def contact(request):
    '''this function is for template activation
    contact us page will display as per this page request.
    
    if only want to display after login then
    try:
        obj=Student.objects.get(id=id)
    except:
        return HttpResponseRedirect("/")

    '''
    
    id = request.session.get('id')
    try:
        obj=Student.objects.get(id=id)
    except:
        pass
    
    return render_to_response('frontend/learnincollge_contact.html',locals(),context_instance=RequestContext(request))


def emailverify(request, username, token):
    try:
        obj = Emailverificationlogs.objects.get(fk_student__username=username)
        studentobj = Student.objects.get(username=username)
        studentobj.verified = True
        studentobj.verifiedat = datetime.now()
        studentobj.save()
        obj.delete()
    except:
        return HttpResponse("Already Verified")
    return HttpResponse("Mail is successfully verified")



class PasswordReset(TemplateView):
    def get(self,request):
        return render_to_response('frontend/forgot_password.html',locals(),context_instance=RequestContext(request))
    
    def post(self,request):
        email=request.POST.get('email')
        if email == "":
            return HttpResponse("Please Provide email address")
        
        
        mailvalidation = is_valid_email(email)
        
        if mailvalidation == False:
            return HttpResponse("Please enter a valid Email Address.")
        
            
        mailavailablity = Student.objects.filter(email=email).exists()
        if mailavailablity == False:
            return HttpResponse("We can't find your email id :P ")
        
        function=GeneralFunctions()
        token = function.Genkey(length=0, chars=string.letters + string.digits)
        
        obj = Student.objects.get(email=email)
        tokenobj = PasswordResetlogs.objects.create(fk_student=obj,token=token,expiretimestamp=datetime.now() + timedelta(minutes=180)
        )
            
        trigger = "PASSWORD_RESET"
        mail= MailSending(obj,trigger)
        
        mail.emailverificationmail(tokenobj)
        
        
        return render_to_response('frontend/forgot_password.html',locals(),context_instance=RequestContext(request))

class PasswordResetAction(TemplateView):
    def get(self,request,username,token ,expireid):
        try:
            obj=Student.objects.get(username=username)
        except:
            return HttpResponse("Invalid link")
        print expireid ,token 
        try:
            tokenobj = PasswordResetlogs.objects.get(id=expireid)
        except:
            import sys
            print sys.exc_info()
            return HttpResponse("Link is not valid now.you have already used this link")
        
        expiretime = tokenobj.expiretimestamp
        
        if expiretime < datetime.now():
            return HttpResponse("Link is being expired.")
        
        
        return render_to_response('frontend/password_reset_action.html',locals(),context_instance=RequestContext(request))

    def post(self,request,username,token,expireid):
        try:
            obj=Student.objects.get(username=username)
        except:
            return HttpResponse("Invalid link")
        try:
            tokenobj = PasswordResetlogs.objects.get(id=expireid,\
                                                     fk_student=obj,token=token,\
                                                     )
        except:
            return HttpResponse("Link is not valid now.you have already used this link")
        
        
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password == "" or cpassword == "":
            return HttpResponse("Password fields can not be blank")
        
                
        if password != cpassword:
            return HttpResponse("Both Values are not same ")
        
        if len(cpassword) < 5 or len(cpassword) > 8 :
            return HttpResponse("password should be between 5 characters to 8 characters.")        
        
        obj = Student.objects.get(username=username)
        
        password = enc_password(cpassword)
        obj.password=password
        obj.save()
        tokenobj.delete()
        return HttpResponseRedirect("/")































    
    
    
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
    
    
    
    
    