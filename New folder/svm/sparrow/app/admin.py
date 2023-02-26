from dataclasses import fields
from django.contrib import admin
from app.models import p_form,supplier,p_master,p_temp,p_dtls
# from app.models import p_form,form
# from app.views import p_form 
# Register your models here.

class p_formAdmin(admin.ModelAdmin):
    list_display =['id','itemname','rate','brand','date','status']
    # list_display = ('title', 'author', 'price')
admin.site.register(p_form,p_formAdmin)


admin.site.register(supplier),
admin.site.register(p_master),
admin.site.register(p_temp),
admin.site.register(p_dtls),
