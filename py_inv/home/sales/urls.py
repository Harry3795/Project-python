from django.urls import path,re_path
from sales import views
from sales.views import *

urlpatterns = [
    # path('sales/',views.sales_page),
    re_path(r'sales_list/$', salesList, name='salesList'),
    re_path(r'getItems_details/$', getItems_details, name='getItems_details'),
    re_path(r'getItems_available/$', getItems_available, name='getItems_available'),
    # re_path(r'ajaxqty/$', ajaxqty, name='ajaxqty'),
    re_path(r'sales_master/(?P<action>\w+)/(?P<ids>(.*)+|)$', sales),
    re_path(r'sales_view/(?P<action>\w+)/(?P<ids>(.*)+|)$', sales_view, name='sales_view'),

]