from urllib import request
from django.shortcuts import render,redirect
from .forms import ItemForm,SupplierForm
from .models import items,supplier
from django.contrib import messages
# from app.models import items,suppplier


# Create your views here.
def index(request):
    return render(request,'index.html')
def insert_item(request):
    
    if request.method=='POST':
        form=ItemForm(request.POST)
        if form.is_valid():
            # itm=form.cleaned_data['itemname']
            # rate=form.cleaned_data['rate']
            # brand=form.cleaned_data['brand']
            # tdate=form.cleaned_data['tdate']
            # status=form.cleaned_data['status']
            form.save()
            return redirect('/index')
            messages.success(request, 'Form submission successful')
            return redirect('/insert_item')
            
    else:
        form=ItemForm()
        
    return render(request,'insert_item.html',{'form':form})
def supplier_add(request):
    
    if request.method=='POST':
        sform=SupplierForm(request.POST)
        if sform.is_valid():
            sname=sform.cleaned_data['sname']
            semail=sform.cleaned_data['email']
            spass=sform.cleaned_data['password']
            sadd=sform.cleaned_data['address']
            supp_dtls=supplier(sname=sname,email=semail,password=spass,address=sadd)
            supp_dtls.save()
            
            messages.success(request, 'Form submission successful')
            return redirect('/index')
            
    else:
        sform=SupplierForm()
        s_fetch_details=supplier.objects.all()
        
    return render(request,'supplier_add.html',{'sform':sform,'sdtls':s_fetch_details})
def supp_list(request):
    
    if request.method=='POST':
        sform=SupplierForm(request.POST)
        if sform.is_valid():
            sname=sform.cleaned_data['sname']
            semail=sform.cleaned_data['email']
            spass=sform.cleaned_data['password']
            sadd=sform.cleaned_data['address']
            sform.save()
            
            messages.success(request, 'Form submission successful')
            return redirect('/index')
            
    else:
        sform=SupplierForm()
        s_fetch_details=supplier.objects.all()
        
    return render(request,'supp_list.html',{'sform':sform,'sdtls':s_fetch_details})
def item_list(request):
    item_fetch_dtls=items.objects.all()
    return render(request,'item_list.html',{'itm_dtls':item_fetch_dtls})
def views_item(request,id):
    item_fetch_dtls_single=items.objects.get(pk=id)
    
    return render(request,'item_single_view.html',{'itm_single':item_fetch_dtls_single})


