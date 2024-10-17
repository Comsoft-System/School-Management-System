from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-site/', admin.site.urls),
    path('', include('student.urls')),
    path('', include('fee.urls')),
]