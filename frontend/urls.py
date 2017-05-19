from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os
from frontend.views import *


urlpatterns = [       
    url(r'^$', index, name='index'),            
    #url(r'^jsoncheck/$', 'frontend.views.jsoncheck', name='jsoncheck'),        
    url(r'^student-signin/$', signin, name='studentsignin'),   
    url(r'^signup-step1/$', SignupStep1.as_view(), name='signupstep1'),
    url(r'^passwordreset/$', PasswordReset.as_view(), name='passwordreset'),
    url(r'passwordresetaction/(?P<username>\w.+)/(?P<token>\w+)/(?P<expireid>\w+)/$', PasswordResetAction.as_view(),name="passwordresetaction"),    
    url(r'^emailverificationresponse/(?P<username>\w+)/(?P<token>\w+)/$', emailverify, name='emailverify'),        
    url(r'^signup-step2/$', signupstep2, name='signupstep2'),
    url(r'^signup-step3/$', signupstep3, name='signupstep3'),
    url(r'^adddepartmentmanually/$', signupstep3, name='adddepartment'),
    url(r'^addintrestmanually/$', signupstep2, name='addintrest'),        
    url(r'^signup-step2/(?P<intrestid>\w+)/$', signupstep22, name='signupstep22'),
    url(r'^checkuseravailability/(?P<username>\w+)/$', checkuseravailability, name='checkuseravailability'),
    url(r'^checkemailavailability/(?P<email>\w.+)/$', checkemailavailability, name='checkemailavailability'),   
    url(r'^submitlikequestion/(?P<id>\w+)/(?P<student>\w+)/$', submitlike, name='submitlike'),
    url(r'^submitunlikequestion/(?P<id>\w+)/(?P<student>\w+)/$', submitunlike, name='submitunlike'),            
    url(r'^seeelikestudents/(?P<id>\w+)/$', seestudentlike, name='seestudent-like'),
    url(r'^submit_answer/(?P<id>\w+)/$', submitanswer, name='submitanswer'),            
    url(r'^home/(?P<username>\w+)/$', home, name='home'),        
    url(r'^ask-question/$', ask_question, name='ask-question'),
    url(r'^question/(?P<id>\w+)$', questiondetails, name='question-details'),        
    url(r'^signup-step3/(?P<departmentid>\w+)/$', signupstep32, name='signupstep32'),
    url(r'^profile/(?P<username>\w.+)/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),       
#    url(r"^login/user/(?P<user_id>.+)/$", "user_login", name="loginas-user-login"),    
    url(r'^contact/$', contact, name='contact')
]    





