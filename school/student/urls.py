from django.urls import path
from . import views

urlpatterns = [
    # Front Pages
    path('home/', views.home, name = 'home'),

    # Class Pages
    path('classes/', views.classes, name = 'classes'),
    path('class-add/', views.classAdd, name = 'class_add'),
    path('class-edit/<id>', views.classEdit, name = 'class_edit'),

    # Section Pages
    path('section/', views.section, name = 'section'),
    path('section-add/', views.sectionAdd, name = 'section_add'),
    path('section-edit/<id>', views.sectionEdit, name = 'section_edit'),
    
    # Session Pages
    path('session/', views.session, name = 'session'),
    path('session-add/', views.sessionAdd, name = 'session_add'),
    path('session-edit/<id>', views.sessionEdit, name = 'session_edit'),

    # GR Register Pages
    path('gr-register/', views.grRegister, name = 'gr_register'),
    path('gr-register-add/', views.grRegisterAdd, name = 'gr_register_add'),
    path('gr-register-edit/<id>/', views.grRegisterEdit, name = 'gr_register_edit'),

    # Class Register Pages
    path('class-register/', views.classRegister, name = 'class_register'),
    path('class-register-add/', views.classRegisterAdd, name = 'class_register_add'),
    path('class-register-edit/<id>', views.classRegisterEdit, name = 'class_register_edit'),
]