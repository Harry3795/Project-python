from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from purchase.forms import *
import json
from django.http import JsonResponse
import datetime

# Create your views here.
def purchaseList(request):

    sql = """Select tpm.*,tsm.supplier_name
        from purchase_purchase_mastermodel as tpm join supplier_suppliermastermodel as tsm on tpm.supplier_id=tsm.id order by tpm.id """
    purchaselist = Purchase_MasterModel.objects.raw(sql)
    tempdel = Purchase_tempModel.objects.all().delete()

    if 'DelData' in request.POST:
        DelData = request.POST.get('DelData')
        form = Purchase_MasterModel.objects.filter(id=DelData).update(status=0)
        messages.error(request, 'Document Type Deleted Successfully')

    return render(request, 'purchaseList.html', {'purchaselist': purchaselist})


def purchase(request,action,ids=None):
    form = purchaseForm()
    itemform = purchaseDetailsForm()
    # tempform = purchaseTempForm()
    sql = """Select tp.*,im.item_name,im.id as item_id 
        from purchase_purchase_tempmodel as tp join items_itemmastermodel as im on tp.item_id=im.id """
    templist = Purchase_tempModel.objects.raw(sql)
    y=" "
    if action == 'Save':    
       if request.method == 'POST':
            
        
        if 'add-btn' in request.POST:
            # itemform = purchaseDetailsForm(request.POST, initial=initialdata)
            
            temp=Purchase_tempModel.objects.create(
                item_id=request.POST["item_id"],
                rate=request.POST["rate"],
                qty=request.POST["qty"],
                total=request.POST["total"]
            )
        else:    
            invoice_no = request.POST['invoice_no']
            invoice_date = request.POST['invoice_date']
            supplier_id = request.POST['supplier_id']
            initialdata = {'invoice_no':invoice_no,'invoice_date':invoice_date,'supplier_id':supplier_id}
            form = purchaseForm(request.POST, initial=initialdata)
            
        if 'add' in request.POST:
            f = purchaseForm(request.POST)
            if f.is_valid():
                # item_id=item_id=request.POST["item_id"]
                found = Purchase_MasterModel.objects.filter(status=1,invoice_no=request.POST["invoice_no"]).first()
                if found:
                            messages.error(request, " Invoice No Already Exist")  
                else:
                    add = Purchase_MasterModel.objects.create(
                        invoice_no=request.POST["invoice_no"],
                        invoice_date=datetime.datetime.strptime(request.POST["invoice_date"],'%m/%d/%Y').date(),
                        supplier_id=request.POST["supplier_id"]
                    )
                    recordTemp1 = Purchase_tempModel.objects.filter(id=item_id,item_id=request.POST["item_id"]).first()

                    if recordTemp1:
                        messages.error("item name is already exist please select another")
                    else:   
                        recordTemp=Purchase_tempModel.objects.all()

                        item_id = request.POST.getlist('item_id')
                        qty = request.POST.getlist('qty')
                        rate = request.POST.getlist('rate')
                        total = request.POST.getlist('total')

                        for val in recordTemp:
                            add_details = PurchaseDetailsModel.objects.create(
                                purchase_master_id=add.id,
                                item_id=val.item_id,
                                qty=val.qty,
                                rate=val.rate,
                                total=val.total,
                            )
                            tempdel = Purchase_tempModel.objects.filter(id=val.id,).delete()

                    return redirect('/purchase/purchase_list')


    return render(request, 'purchase.html', {'forms':form, 'action':action, 'itemform' : itemform, 'list': templist,'readlist':y})


def purchase_view(request,action,ids=id):
   
    
    if action == 'Read':
       
        pr = Purchase_MasterModel.objects.filter(id=ids).all().select_related('supplier')

        # print(x)
        # return HttpResponse(x)
        pd2 = PurchaseDetailsModel.objects.filter(purchase_master_id=ids).all().select_related('item')
        

    return render(request,'purchase_view.html',{'action':action, 'master':pr , 'readlist':pd2})

    

def getSupplierDetails(request):
   
    supplier = request.POST.get('supplier_id')
    data_supp = SupplierMasterModel.objects.filter(id=supplier).first()
  
    responseData = { 'status': 'success', 'address': data_supp.address ,'city': data_supp.city, 'pincode': data_supp.pincode,'state': data_supp.state}
    return HttpResponse(json.dumps(responseData))
   

def getItems_details(request):
       
    items = request.POST.get('item_id')
    data_item = ItemMasterModel.objects.filter(id=items).first()

    responseData = {'rate': float(data_item.rate) }
    return HttpResponse(json.dumps(responseData))
   
