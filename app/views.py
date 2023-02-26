from ast import If
import datetime
# from ssl import _PasswordType
from urllib.request import Request
from django.shortcuts import render,HttpResponse,redirect
from app import models
from app.models import p_form, p_master, supplier
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User,AnonymousUser 
from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
     
# username pradeep and password Harry@37
# Create your views here.
def index(request):
    # print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
            # context={
            #     'variable':"this is variable 95"  
            # }
            # return  render(request,'index.html',context)
            
            # return HttpResponse("this is harry the great")
def loginuser(request):
    if request.method=="POST": 
        username=request.POST.get('username')
        password=request.POST.get('password')
        #--------------------------- cheking the authentification user and _Password------------------------------------------
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return  render(request,'login.html')
    return  render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect("/login")
    # return  render(request,'index.html')
def registration(request):
    return  render(request,'registration.html')
def list_item(request):

    itemsdetails=p_form.objects.all()
    return  render(request,'list_item.html',{'item':itemsdetails})
def s_list(request):#supplier displaying all data in dictionarry formate   sdtls-----------------------------
    sdtls=supplier.objects.all()
    return  render(request,'supplier.html',{'sdtls':sdtls})
    # ----------------supplier inserting data or register------------------------------------
def supp_add(request):
    s_data=""
    if request.method=="POST":
        sname=request.POST['sname']
        sname=request.POST['sname']
        semail=request.POST['semail']
        smob=request.POST['smob']
        sadd=request.POST['sadd']
        sdate=request.POST['sdate']
        s_dtls=supplier(sname=sname,semail=semail,smob=smob,sadd=sadd,sdate=sdate)
        s_dtls.save()   
        s_data=supplier.objects.all()
        messages.success(request, 'ONE SUPPLIER IS ADDED SUCCEFULLY')
        
    return  render(request,'supp_add.html',{'s_data':s_data})
def sale(request):
    return  render(request,'sale.html')
def report_stock(request):
    return  render(request,'report_stock.html')
def p_list(request):
    return  render(request,'p_list.html')

def form_purchase(request):
    data=""
    
    if request.method=="POST":
        invoice=request.POST['invoice']
        invoicedate=request.POST['invoicedate']
        sname=request.POST['sname']
        sadd=request.POST['add']
        pmasteradd=p_master(invoice=invoice,invoicedate=invoicedate,sname=sname,sadd=sadd)
        pmasteradd.save()
        data=p_master.objects.all()
  
    return render(request,'form_purchase.html',{'data':data})
def purchase_temp(request,pmasteradd):
    data=""
    if request.method=="POST":
        itemname=request.POST['itamname']
        rate=request.POST['rate']
        qty=request.POST['qty']
        total=request.POST['total']
        invoicedate=request.POST['invoicedate']
        ptemp=p_temp(itamame=itemname,rate=rate,qty=qty,total=total,invoicedate=invoicedate)
        ptemp.save()
        data=p_temp.objects.all()
        def purchase_dtls(request,pmasteradd):
            data=""
            if request.method=="POST":
                itemname=request.POST['itamname']
                rate=request.POST['rate']
                qty=request.POST['qty']
                total=request.POST['total']
                invoicedate=request.POST['invoicedate']
                p_dtls=p_dtls(itamame=itemname,rate=rate,qty=qty,total=total,invoicedate=invoicedate)
                p_dtls.save()
                data=p_dtls.objects.all()
                
            return render(request,'form_purchase.html',{'p_dtls_data':data})
        p_temp=delete()
        
    return render(request,'p_list.html',{'ptemp':ptemp}) 


    
    # -----------------------inserting items----------------------------------
def pform(request):
    data=""
    if request.method=="POST":
        itemname=request.POST['itemname']
        rate=request.POST['rate']
        brand=request.POST['brand']
        purchase=p_form(itemname=itemname,rate=rate,brand=brand,date=datetime.today())
        purchase.save()
        data=p_form.objects.all()
        messages.success(request, 'ONE ITEM IS ADDED SUCCEFULLY')

    return  render(request,'p_form.html',{'item':data})


    # return HttpResponse("this is harry the great player")
def views(request, id):
    itemviews=p_form.objects.get(id=id)
    return  render(request,'views.html',{'views':itemviews})

    #------------------------- before updattion show items------------------
def update(request, id):
    update=p_form.objects.get(id=id)
    upd_item=p_form.objects.all()
    context = {
        'update': update,
        'upd_item': upd_item
    }
    return  render(request,'update.html',context)
    
    # ----------------------------updated items -------------------------------
def update_item(request, id):
    u=p_form.objects.get(id=id)
    u.itemname=request.POST['itemname']
    u.rate=request.POST['rate']
    u.brand=request.POST['brand']
    u.date=request.POST['date']
    u.save()
    messages.info(request,'item updated succefully')
    return  redirect('list_item')
# --------------------------before delete show items---------------------------------------------------
def delete(request, id):
    del_item=p_form.objects.get(id=id)
    return  render(request,'delete.html',{'delete':del_item})
    # ---------------------------------delete item code-----------------------------
def delete_item(request, id):
    d=p_form.objects.get(id=id)
    # d.itemname=request.POST['itemname']
    # d.rate=request.POST['rate']
    # d.brand=request.POST['brand']
    # d.date=request.POST['date']
    d.delete()
    messages.info(request,'item deleted succefully')
    return  redirect('list_item')
def fetchsupp_add(request,id):
    d=p_form.objects.get(itemname=id)
    form=p_form(request.POST)
    if form.is_valid():
        itemname=request.POST['itemname']
        rate=request.POST['rate']
        rate_fetch=p_form(rate=rate)
        rate_fetch.save()
        
        return JsonResponse({'status':'data'}) 
    else:
        return JsonResponse({'status':0})
    # messages.info(request,'item deleted succefully')
    

    return render(request,'form_purchase.html')
def form_purchase(request):
    itm=p_form.objects.all()
    sup=supplier.objects.all()
    return render(request,'form_purchase.html',{'p_form':itm},{'supplier':sup})
    
def form_purchase(request):
    
    return render(request,'form_purchase.html')
    
