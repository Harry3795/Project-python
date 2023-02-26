from django.urls import path,re_path
from items import views
from items.views import *

urlpatterns = [
    re_path(r'items_master_list/$', itemsList, name='itemsList'),
    re_path(r'items_master/(?P<action>\w+)/(?P<ids>(.*)+|)$', itemsMaster),
]