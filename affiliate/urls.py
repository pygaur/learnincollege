from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^affiliate', home, name='affiliate-home'),
    url(r'^signup-college', signup, name='affiliate-signup'),
    url(r'^signin-college', signin, name='affiliate-signin'),
    url(r'^profile-college', profile, name='affiliate-profile'),
    url(r'^edit-profile-college/$', editprofile, name='affiliate-editprofile'),
    url(r'^edit-profile-college-extra', editprofileextra, name='affiliate-editprofileextra'),
    url(r'^campaign-college', campaign, name='affiliate-campaign'),    
    url(r'^change-password-college', passwordchange, name='affiliate-passwordchange'),
    url(r'^reset-password-college', passwordreset, name='affiliate-passwordreset'),
    url(r'^logout-college', logout, name='affiliate-logout'),   
]   




