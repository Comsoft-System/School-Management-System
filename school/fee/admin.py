from django.contrib import admin
from .models import FeeType, Concession, ClassFee, Fee

@admin.register(FeeType)
class AdminFeeType(admin.ModelAdmin):
    list_display = ['fee_code', 'fee_type', 'fee_remarks']

@admin.register(Concession)
class AdminConcession(admin.ModelAdmin):
    list_display = ['concession_code', 'concession_type', 'concession_amount','concession_persent','concession_remarks']

@admin.register(ClassFee)
class AdminClassFee(admin.ModelAdmin):
    list_display = ['class_code', 'fee_amount']

@admin.register(Fee)
class AdminFee(admin.ModelAdmin):
    list_display = ['gr_number', 'class_code', 'section_code','due_amount','submit_amount','fee_status',]
