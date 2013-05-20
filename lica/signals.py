from datetime import datetime

def onlogin(sender , instance , created , **kwargs):
    if created == True:
        try:
            from lica.models import Loginlogs
            loginobj = Loginlogs.objects.filter(fk_student=instance.fk_student,loginok = True,timestamp__day=datetime.now().day,timestamp__month=datetime.now().month,timestamp__year=datetime.now().year).count()
        except:
            import sys
            print sys.exc_info()
        print loginobj    
        if loginobj == 0:
            instance.uniquelogin = True
            instance.save()
        #
    

