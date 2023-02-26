from django.urls import path,re_path
from system import views
from system.views import *

urlpatterns = [
    path('system/',views.index_page),
    re_path(r'report/$', stockReport, name='stockReport'),
    
]