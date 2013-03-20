from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import frontend
import os



urlpatterns = patterns('',
    url(r'^affiliate', 'affiliate.views.home', name='affiliate-home'),
    url(r'^signup-college', 'affiliate.views.signup', name='affiliate-signup'),
    url(r'^signin-college', 'affiliate.views.signin', name='affiliate-signin'),
    url(r'^profile-college', 'affiliate.views.profile', name='affiliate-profile'),
    url(r'^edit-profile-college/$', 'affiliate.views.editprofile', name='affiliate-editprofile'),
    url(r'^edit-profile-college-extra', 'affiliate.views.editprofileextra', name='affiliate-editprofileextra'),
    url(r'^campaign-college', 'affiliate.views.campaign', name='affiliate-campaign'),
    
    url(r'^change-password-college', 'affiliate.views.passwordchange', name='affiliate-passwordchange'),
    url(r'^reset-password-college', 'affiliate.views.passwordreset', name='affiliate-passwordreset'),
    url(r'^logout-college', 'affiliate.views.logout', name='affiliate-logout'),
    
    url(r'^admin/', include(admin.site.urls)),
    
    
    
    

)




