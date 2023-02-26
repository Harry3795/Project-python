from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('insert_item',views.insert_item,name="insert_item"),
    path('item_list',views.item_list,name="item_list"),
    path('supplier_add',views.supplier_add,name="supplier_add"),
    path('supp_list',views.supp_list,name="supp_list"),
    path('views_item',views.views_item,name="views_item"),
]