import os
import sys
path = '/home/menmine/Documents'
if path not in sys.path:   
    sys.path.append(path)
    sys.path.insert(0,"/home/menmine/Documents/collegeportal")
#os.environ['DJANGO_SETTINGS_MODULE'] = 'collegeportal.settings'

import settings

import django.core.management
django.core.management.setup_environ(settings)
utility = django.core.management.ManagementUtility()
command = utility.fetch_command('runserver')
    
command.validate()

import django.conf 
import django.utils
    
django.utils.translation.activate(django.conf.settings.LANGUAGE_CODE)
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
