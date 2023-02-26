from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db import connection
from .models import *
from django.db.models import Sum
# from django.db.models import ItemMasterModel
import datetime

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

# def stockReport(request):

#     cursor = connection.cursor()
#     query = """select tbl_items_master.*,COALESCE(total_pur_qty,0) as total_pur_qty,COALESCE(total_sale_qty,0) as total_sale_qty,
#             (COALESCE(total_pur_qty,0)-COALESCE(total_sale_qty,0)) as balance_stock from tbl_items_master
#             LEFT JOIN( SELECT item_id,sum(qty) as total_pur_qty from tbl_purchase_details group by item_id order by item_id)as purchase on purchase.item_id=tbl_items_master.id
#             LEFT JOIN( SELECT item_id,sum(qty) as total_sale_qty from tbl_sales_details group by item_id order by item_id)as sale on sale.item_id=tbl_items_master.id WHERE tbl_items_master.status=1"""
#     cursor.execute(query)
#     stock_list = cursor.fetchall()
#     return render(request, 'stockReport.html')


def stockReport(request):
    res=''
    fromDate=datetime.date.today()
    toDate=datetime.date.today()
    if request.method=='POST':
        fromDate=request.POST.get('txtFromDate')
        toDate=request.POST.get('txtToDate')
        sql="""SELECT 1 as id,im.item_name, coalesce(purchase_qty, 0) as purchase_qty, coalesce(sale_qty, 0) as sale_qty, 
                (coalesce(purchase_qty, 0) - coalesce(sale_qty, 0)) as current_stock from tbl_items_master im 
                left join ( \n  
                    SELECT sum(pd.qty) as purchase_qty,pd.item_id
                    from tbl_purchase_details pd
                    join tbl_purchase_master as pm on pm.id=pd.purchase_master_id
                    where invoice_date BETWEEN '%s' and '%s' group by item_id
                ) purchase_detail  on purchase_detail.item_id = im.id 
                left join ( \n  
                    SELECT sum(qty) as sale_qty, item_id from tbl_sales_details sd
                    join tbl_sales_master as sm  on sm.id=sd.sales_master_id  
                    where sales_date BETWEEN '%s' and '%s' group by item_id
                ) 
                sale_detail  on sale_detail.item_id = im.id 
                where status=1 group by im.id,im.item_name,purchase_qty,sale_qty"""%(fromDate,toDate,fromDate,toDate)
        res = ItemMasterModel.objects.raw(sql)
        print(res.query)
        # return HttpResponse(res.query)
    return render(request,'stockReport.html',{'res': res})

def ajaxqty(request):
    item_id=request.POST.get("item_id")
    print(item_id)
    purqty=PurchaseDetail.objects.filter(item_master_id=item_id).aggregate(Sum('quantity'))
    if purqty['quantity__sum'] is None:
        purqty = 0
    else:
        purqty = purqty['quantity__sum']
    salqty=SellDetail.objects.filter(item_master_id=item_id).aggregate(Sum('quantity'))
    if salqty['quantity__sum'] is None:
        salqty = 0
    else:
        salqty = salqty['quantity__sum']
    qnty=purqty-salqty
    # qnty=purqty
    print(qnty,"quantity")
    option='<option value="">Select Quantity</option>'
    if qnty is not None:
        for qty in range(1,qnty + 1):
            option+='<option value="'+str(qty)+'">'+str(qty)+'</option>'
    option1=qnty
    return JsonResponse(option1,safe=False)
