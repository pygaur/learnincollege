from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import os
from frontend.models import *
from lica.models import *
from lica.views import *



urlpatterns = patterns('',
    url(r'^$', Dashboard.as_view(), name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
    )




