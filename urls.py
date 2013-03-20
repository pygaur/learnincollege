from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import frontend
import os

static_files = os.path.join(
    os.path.dirname(__file__) , 'static_files'
)


urlpatterns = patterns('',
    
    url(r'^', include('frontend.urls')),
    url(r'^', include('affiliate.urls')),
    
    # Examples:
    # url(r'^$', 'collegeportal.views.home', name='home'),
    # url(r'^collegeportal/', include('collegeportal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^static_files/(?P<path>.*)$' , 'django.views.static.serve' ,
        {'document_root' : static_files }),

)

urlpatterns += patterns('loginas.views',
    url(r"^login/user/(?P<user_id>.+)/$", "user_login", name="loginas-user-login"),
)
