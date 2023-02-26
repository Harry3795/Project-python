from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
        path('',views.index,name='home'),
        # path('about',views.about,name='about'),
        path('login',views.loginuser,name='login'),
        path('logout',views.logoutuser,name='logout'),
        path('index',views.index,name='index'),
        # path('registration',views.registration,name='registation'),
        path('list_item',views.list_item,name='list_item'),
        path('supplier',views.s_list,name='supplier'),
        path('supp_add',views.supp_add,name='supp_add'),
        path('p_list',views.p_list,name='p_list'),
        path('p_dtls/<id>',views.p_list,name='p_list'),
        path('sale',views.sale,name='sale'),
        path('report_stock',views.report_stock,name='report'),
        path('p_form',views.pform,name='pform'),
        path('views/<int:id>',views.views,name='views'),
        path('update/<int:id>',views.update,name='update'),
        path('update_item/<int:id>',views.update_item,name='update_item'),
        path('delete/<int:id>',views.delete,name='delete'),
        path('delete_item/<int:id>',views.delete_item,name='delete_item'),
        path('form_purchase',views.form_purchase,name='form_purchase'),
        path('fatchajax',views.fatchajax,name='fatchajax'),
        
 
]