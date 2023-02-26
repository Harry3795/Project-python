from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from supplier.forms import *

# Create your views here.
def supplierList(request):
    supplierlist = SupplierMasterModel.objects.all().filter(status=1).order_by('id')  
    # print(supplierlist)
    # return HttpResponse(supplierlist) 

    if 'DelData' in request.POST:
        DelData = request.POST.get('DelData')
        form = SupplierMasterModel.objects.filter(id=DelData).update(status=0)
        messages.error(request, 'Document Type Deleted Successfully')

    return render(request, 'supplierList.html', {'suppierList': supplierlist})


def supplierMaster(request,action,ids=None):
    error_msg=" "
    form = supplierMasterForm()
    if action == 'Save':
        if request.method == 'POST':
            form = supplierMasterForm(request.POST)
            
                # return HttpResponse(request.POST) 
                
            ins=SupplierMasterModel.objects.create(
                supplier_name=request.POST["supplier_name"],
                mobile=request.POST["mobile"],
                address=request.POST["address"],
                city=request.POST["city"],
                state=request.POST["state"],
                pincode=request.POST["pincode"]
            )
            messages.success(request, 'Data Added Successfully')
            return redirect('/supplier/supplier_master_list')

            # else:
            #     error_msg = "Error!!"

    elif action == 'Update':
        x = SupplierMasterModel.objects.get( id = ids) 
        form = supplierMasterForm(request.POST or None, instance=x)
        if request.method == 'POST':
            form = supplierMasterForm(request.POST, instance=x)
            # if form.is_valid():
            update_ins=SupplierMasterModel.objects.filter(id=ids).update(
                supplier_name=request.POST["supplier_name"],
                mobile=request.POST["mobile"],
                address=request.POST["address"],
                city=request.POST["city"],
                state=request.POST["state"],
                pincode=request.POST["pincode"]
                )
            messages.success(request, 'Data Updated Successfully')
            return redirect('/supplier/supplier_master_list')
                                      
            # else:
            #     error_msg = "Error!!"
        

    return render(request, 'supplierMaster.html', {'forms':form, 'action':action,'error_msg':error_msg})
