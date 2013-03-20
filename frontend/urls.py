from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import frontend
import os



urlpatterns = patterns('',
    url(r'^$', 'frontend.views.index', name='index'),
    #url(r'^jsoncheck/$', 'frontend.views.jsoncheck', name='jsoncheck'),
    
    
    url(r'^student-signin/$', 'frontend.views.signin', name='studentsignin'),
    
    url(r'^signup-step1/$', 'frontend.views.signupstep1', name='signupstep1'),
    url(r'^signup-step2/$', 'frontend.views.signupstep2', name='signupstep2'),
    url(r'^signup-step3/$', 'frontend.views.signupstep3', name='signupstep3'),
    url(r'^signup-step2/(?P<intrestid>\w+)/$', 'frontend.views.signupstep22', name='signupstep22'),
    url(r'^checkuseravailability/(?P<username>\w+)/$', 'frontend.views.checkuseravailability', name='checkuseravailability'),
    url(r'^submitlikequestion/(?P<id>\w+)/(?P<student>\w+)/$', 'frontend.views.submitlike', name='submitlike'),
    url(r'^submitunlikequestion/(?P<id>\w+)/(?P<student>\w+)/$', 'frontend.views.submitunlike', name='submitunlike'),
    
    url(r'^seeelikestudents/(?P<id>\w+)/$', 'frontend.views.seestudentlike', name='seestudent-like'),
    
    
    
    url(r'^home/(?P<username>\w+)/$', 'frontend.views.home', name='home'),
    url(r'^ask-question/$', 'frontend.views.ask_question', name='ask-question'),
    url(r'^question/(?P<id>\w+)$', 'frontend.views.questiondetails', name='question-details'),
    
    
    url(r'^signup-step3/(?P<departmentid>\w+)/$', 'frontend.views.signupstep32', name='signupstep32'),
    
    
    # url(r'^collegeportal/', include('collegeportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    
    
    
    url(r'^admin/', include(admin.site.urls)),
    
    
    
    url(r"^login/user/(?P<user_id>.+)/$", "user_login", name="loginas-user-login"),

)



