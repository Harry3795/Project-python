import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from sales.models import *
from sales.forms import *
import datetime
import json
from django.http import JsonResponse


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

   sql = """Select s.*,i.item_name,i.id as item_id 
        from sales_sales_tempmodel as s join items_itemmastermodel as i on s.item_id=i.id """
   templist = Sales_tempModel.objects.raw(sql)

   if action == 'Save':
      if request.method == 'POST':
         sales_no = request.POST['sales_no']
         sales_date = request.POST['sales_date']
         customer_name = request.POST['customer_name']
         # mobile = request.POST['mobile']
         address = request.POST['address']
         initialdata = {'sales_no':sales_no,'sales_date':sales_date,'customer_name':customer_name,
         # 'mobile':mobile,
         'address':address}
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
      x1 = Sales_MasterModel.objects.filter(id=ids).all()

      y2 = SalesDetailsModel.objects.filter(sales_master_id=ids).all().select_related('item')
      # print(y2.query)

   return render(request,'sales_view.html',{'action':action,'master':x1,'readlist':y2})

def getItems_details(request):
       
    items = request.POST.get('item_id')
    data_item = PurchaseDetailsModel.objects.filter(id=items).first()
    responseData = {'rate': float(data_item.rate),}
    print(responseData)
    return HttpResponse(json.dumps(responseData))
def getItems_available(request):
       
    av_qty = request.POST.get('av_qty')
    print(av_qty)
    
    avqty=PurchaseDetailsModel.objects.raw('''
         select  (COALESCE(purchase_qty,0)-COALESCE(sales_qty,0)-COALESCE(tempsales_qty,0)) as av_qty from items_itemmastermodel i 
      left join 
      ( select item_id,sum(pd.qty) as purchase_qty from purchase_purchasedetailsmodel pd group by item_id 
       ) as pur on i.id=pur.item_id 
       left join 
       ( select item_id, COALESCE(sum(s.qty), 0) as sales_qty from sales_salesdetailsmodel s group by item_id
       ) as sal on i.id=sal.item_id 
       left join
       ( select item_id, COALESCE(sum(ts.qty), 0) as tempsales_qty from sales_sales_tempmodel ts group by item_id
       ) as temp on i.id=temp.item_id 
       where i.id='%s'; '''%(av_qty))    
   
     
       
       #j=json.dumps(t.stock_left)
    print(avqty ,"hgfdsadfghj")
    responseData = {'av_qty':av_qty ,}
    return HttpResponse(json.dumps(responseData))

    

# def ajaxqty(request):



   #  qty_id=request.POST.get("qty_id")
   #  print(qty_id)
   #  purqty=PurchaseDetailsModel.objects.filter(item_id=qty_id).aggregate(sum('quantity'))
   #  if purqty['quantity__sum'] is None:
   #      purqty = 0
   #  else:
   #      purqty = purqty['quantity__sum']
   #  salqty=SalesDetailsModel.objects.filter(item_master_id=item_id).aggregate(sum('quantity'))
   #  if salqty['quantity__sum'] is None:
   #      salqty = 0
   #  else:
   #      salqty = salqty['quantity__sum']
   #  qnty=purqty-salqty
   #  # qnty=purqty
   #  print(qnty,"quantity")
   #  option='<option value="">Select Quantity</option>'
   #  if qnty is not None:
   #      for qty in range(1,qnty + 1):
   #          option+='<option value="'+str(qty)+'">'+str(qty)+'</option>'
   #  option1=qnty
   #  return JsonResponse(safe=False)