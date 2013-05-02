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
    tyear = datetime.now().year
    tmonth = datetime.now().month
    tdate = datetime.now().date
    days = 365.25
    
    from datetime import date
    age = int((date.today() - Birthday).days/days)
    return age

def jstopython(Dob):
    print Dob
    month = str(Dob.split('/')[0])
    date = str(Dob.split('/')[1])
    year= str(Dob.split('/')[2])
    a = int(year)
    b =int(month)
    c= int(date)
    from datetime import date
    Dob= date(a,b,c)
    return Dob
    
    
    