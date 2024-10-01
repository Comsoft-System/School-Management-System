from django.contrib import admin
from .models import Classes, Section, Session, GRRegister, ClassRegister

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['class_code', 'class_name']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['section_code', 'section_name']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_code', 'session_name']

@admin.register(GRRegister)
class GRRegisterAdmin(admin.ModelAdmin):
    list_display = ['gr_number', 'name', 'father_name']

@admin.register(ClassRegister)
class ClassRegisterAdmin(admin.ModelAdmin):
    list_display = ['gr_number', 'gr_name', 'gr_father_name']
    
    def gr_name(self, obj):
        return obj.gr_number.name

    def gr_father_name(self, obj):
        return obj.gr_number.father_name

    gr_name.short_description = 'Name'
    gr_father_name.short_description = 'Father Name'