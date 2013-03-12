from django.contrib import admin
from frontend.models import *
class StudentAdmin(admin.ModelAdmin):
    list_display= ['id','username']
admin.site.register(Student , StudentAdmin)

class IntrestAdmin(admin.ModelAdmin):
    list_display= ['intrestfieldname','id','minimumage','maximumage','intrestfieldname']
admin.site.register(Intrest , IntrestAdmin)

class IntrestinfoAdmin(admin.ModelAdmin):
    list_display= ['id','fk_student','fk_intrest']
admin.site.register(Intrestinfo , IntrestinfoAdmin)

class DepartmentinfoAdmin(admin.ModelAdmin):
    list_display= ['id','fk_student','fk_department']
admin.site.register(Departmentinfo , DepartmentinfoAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display= ['departmentname']
admin.site.register(Department , DepartmentAdmin)
    
