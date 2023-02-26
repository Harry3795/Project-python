from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from sales.forms import *
import datetime


# Create your views here.

# def sales_page(request):
#    return render(request, 'index.html')

def salesList(request):

   saleslist = Sales_MasterModel.objects.all().filter(status=1).order_by('id') 

   if 'DelData' in request.POST:
      DelData = request.POST.get('DelData')
      form = Sales_MasterModel.objects.filter(id=DelData).update(status=0)
      messages.error(request, 'Document Type Deleted Successfully')

   return render(request, 'salesList.html', {'saleslist': saleslist})



def sales(request,action,ids=None):
   form = salesForm()
   saleitem = salesDetailsForm()

   sql = """Select ts.*,im.item_name,im.id as item_id 
        from tbl_temp_sales as ts join tbl_items_master as im on ts.item_id=im.id """
   templist = Sales_tempModel.objects.raw(sql)

   if action == 'Save':
      if request.method == 'POST':
         sales_no = request.POST['sales_no']
         sales_date = request.POST['sales_date']
         customer_name = request.POST['customer_name']
         mobile = request.POST['mobile']
         address = request.POST['address']
         initialdata = {'sales_no':sales_no,'sales_date':sales_date,'customer_name':customer_name,'mobile':mobile,'address':address}
         form = salesForm(request.POST, initial=initialdata)

         if 'add-btn' in request.POST:
            saleitem = salesDetailsForm(request.POST, initial=initialdata)
            
            temp=Sales_tempModel.objects.create(
               item_id=request.POST["item_id"],
               rate=request.POST["rate"],
               qty=request.POST["qty"],
               total=request.POST["total"]
            )

         if 'add' in request.POST:
            add = Sales_MasterModel.objects.create(
               sales_no=request.POST["sales_no"],
               sales_date=datetime.datetime.strptime(request.POST["sales_date"],'%m/%d/%Y').date(),
               customer_name=request.POST["customer_name"],
               mobile=request.POST["mobile"],
               address=request.POST["address"]
            )

            recordTemp = Sales_tempModel.objects.all()

            item_id = request.POST.getlist('item_id')
            qty = request.POST.getlist('qty')
            rate = request.POST.getlist('rate')
            total = request.POST.getlist('total')

            for val in recordTemp:
               add_details = SalesDetailsModel.objects.create(
                  sales_master_id=add.id,
                  item_id=val.item_id,
                  qty=val.qty,
                  rate=val.rate,
                  total=val.total,
               )
               tempdel = Sales_tempModel.objects.filter(id=val.id,).delete()

            return redirect('/sales/sales_list')

   return render(request, 'sales.html', {'forms':form, 'action':action,'saleitem': saleitem, 'list':templist})

def sales_view(request,action,ids=id):
   if  action == 'Read':
      x = Sales_MasterModel.objects.filter(id=ids).all()

      y = SalesDetailsModel.objects.filter(sales_master_id=ids).all().select_related('item')

   return render(request,'sales_view.html',{'action':action,'master':x,'readlist':y})