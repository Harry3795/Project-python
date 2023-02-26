from django.urls import path,re_path
from purchase import views
from purchase.views import *

urlpatterns = [
    re_path(r'purchase_list/$', purchaseList, name='purchaseList'),
    re_path(r'purchase_master/(?P<action>\w+)/(?P<ids>(.*)+|)$', purchase),
    re_path(r'getSupplier_details/$', getSupplierDetails, name='getSupplierDetails'),
    re_path(r'getItems_details/$', getItems_details, name='getItems_details'),
    re_path(r'purchase_view/(?P<action>\w+)/(?P<ids>(.*)+|)$', views.purchase_view, name='purchase_view'),
]