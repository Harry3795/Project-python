from django.urls import path,re_path
from supplier import views
from supplier.views import *


urlpatterns = [
    re_path(r'supplier_master_list/$', supplierList, name='supplierList'),
    re_path(r'supplier_master/(?P<action>\w+)/(?P<ids>(.*)+|)$', supplierMaster),
    
]
