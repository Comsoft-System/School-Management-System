from django.urls import path
from . import views

urlpatterns = [
    # Fee Type
    path('fee-type/',views.feeType, name='fee_type'),
    path('fee-type-add/',views.feeTypeAdd, name='fee_type_add'),
    path('fee-type-edit/<id>',views.feeTypeEdit, name='fee_type_edit'),

    # Concession
    path('concession/',views.concession, name='concession'),
    path('concession-add/',views.concessionAdd, name='concession_add'),
    path('concession-edit/<id>',views.concessionEdit, name='concession_edit'),

    # Class Fee
    path('class-fee/',views.classFee, name='class_fee'),
    path('class-fee-add/',views.classFeeAdd, name='class_fee_add'),
    path('class-fee-edit/<class_name>',views.classFeeEdit, name='class_fee_edit'),

    # Fee
    path('fee/',views.fee, name='fee'),
    path('fee-submit/',views.feeSubmit, name='fee_submit'),
    path('get-due-amount/<int:gr_number>/', views.getDueAmount, name='get_due_amount'),
    path('get-class-code/<int:gr_number>/', views.getClassCode, name='get_class_code'),
    path('get-section/<int:gr_number>/', views.getSection, name='get_section'),
]