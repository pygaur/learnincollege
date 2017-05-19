from django.contrib import admin
from lica.models import *

class MessagesettingsAdmin(admin.ModelAdmin):
    list_display=['id']
    class Media:
        js=("/static/js/tiny_mce/tiny_mce.js",'/static/js/admin_textareas.js')
    
    
admin.site.register(Messagesettings , MessagesettingsAdmin)

class MessagetriggersAdmin(admin.ModelAdmin):
    list_display=['id']
admin.site.register(Messagetriggers , MessagetriggersAdmin)    


class BonussettingAdmin(admin.ModelAdmin):
    list_display=['bonusname']
admin.site.register(Bonussetting , BonussettingAdmin)    


class BonustriggerAdmin(admin.ModelAdmin):
    list_display=['id']
admin.site.register(Bonustrigger , BonustriggerAdmin)    

    
class LoginlogsAdmin(admin.ModelAdmin):
    list_display=['id','timestamp','loginip','loginok','uniquelogin']
admin.site.register(Loginlogs , LoginlogsAdmin)    
