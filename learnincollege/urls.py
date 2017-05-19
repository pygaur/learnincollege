"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os

from django.conf.urls import url
from django.contrib import admin

static_files = os.path.join(
    os.path.dirname(__file__) , 'static_files'
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('frontend.urls')),
    url(r'^', include('affiliate.urls')),
    url(r'^lica/', include('lica.urls')),
    url(r'', include('social_auth.urls')),
]

urlpatterns += patterns('loginas.views',
    url(r"^login/user/(?P<user_id>.+)/$", "user_login", name="loginas-user-login"),
)
