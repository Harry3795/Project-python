def get_value_for_stock_left_sale(request):
    un=request.GET['un']
    
    t=Purchase_details.objects.raw('''
         select i.id, (COALESCE(purchase_qty,0)-COALESCE(sales_qty,0)-COALESCE(tempsales_qty,0)) as av_qty from items_itemmastermodel i 
      left join 
      ( select item_id,sum(pd.qty) as purchase_qty from purchase_purchasedetailsmodel pd group by item_id 
       ) as pur on i.id=pur.item_id 
       left join 
       ( select item_id, COALESCE(sum(s.qty), 0) as sales_qty from sales_salesdetailsmodel s group by item_id
       ) as sal on i.id=sal.item_id 
       left join
       ( select item_id, COALESCE(sum(ts.qty), 0) as tempsales_qty from sales_sales_tempmodel ts group by item_id
       ) as temp on i.id=temp.item_id 
       where i.id='%s'; '''%(un))    
       
       #j=json.dumps(t.stock_left)
       
    return render(request,'stock_left.html',{'t':t})

