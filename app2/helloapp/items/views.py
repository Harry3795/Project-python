from django.shortcuts import render
from django.views.generic import TemplateView
from items.forms.itemsforms import *
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def itemsList(request):
    
    itemslist = ItemMasterModel.objects.all().filter(status=1).order_by('id')
    #print(itemslist)
    #return HttpResponse(itemslist)

    if 'DelData' in request.POST:
        DelData = request.POST.get('DelData')
        form = ItemMasterModel.objects.filter(id=DelData).update(status=0)
        messages.error(request, 'Document Type Deleted Successfully')
    
    return render(request, 'itemsList.html', {'itemsList': itemslist})


def itemsMaster(request,action,ids=None):
    error_msg=" "
    form = itemsMasterForm()
    
    if action == 'Save':
        if request.method == 'POST':
            form = itemsMasterForm(request.POST)
            if form.is_valid():
                #print(request.POST)
                #return HttpResponse(request.POST) 
                found = ItemMasterModel.objects.filter(status=1,item_name=request.POST["item_name"]).first()
                if found:
                    messages.error(request, " Already Exists")
                    
                else:
                    ins=ItemMasterModel.objects.create(
                        brand_name=request.POST["brand_name"],
                        item_name=request.POST["item_name"],
                        rate=request.POST["rate"]
                    )
                    if ins.id>0:
                        #print('okkkkkkkkkkkkkk')
                        messages.success(request, 'Data Added Successfully')
                        return redirect('/items/items_master_list')
            else:
                error_msg = "Error!!"

    elif action == 'Update':
        x = ItemMasterModel.objects.get( id = ids) 
        form = itemsMasterForm(request.POST or None, instance=x)
        if request.method == 'POST':
            form = itemsMasterForm(request.POST, instance=x)
            if form.is_valid():
                update_ins=ItemMasterModel.objects.filter(id=ids).update(
                    brand_name=request.POST["brand_name"],
                    item_name=request.POST["item_name"],
                    rate=request.POST["rate"]
                    )
                messages.success(request, 'Data Updated Successfully')
                return redirect('itemsList')
                                      
            else:
                error_msg = "Error!!"              

    return render(request, 'itemsMaster.html', {'forms':form, 'action':action,'error_msg':error_msg})