import random
#from django.contrib.auth.models import get_hexdigest
from datetime import datetime ,  date


#def enc_password(password):
#    algo = 'sha1'
#    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
#    hsh = get_hexdigest(algo, salt, password)
#    password = '%s$%s$%s' % (algo, salt, hsh)
#    return password


def ageverify(Birthday):
    year = str(Birthday.split('-')[0])
    month = str(Birthday.split('-')[1])
    date= str(Birthday.split('-')[2])
    a = int(year)
    b =int(month)
    c= int(date)
    tyear = datetime.now().year
    tmonth = datetime.now().month
    tdate = datetime.now().date
    days = 365.25
    
    from datetime import date
    bir = date(a,b,c)
    age = int((date.today() - bir).days/days)
    return age

