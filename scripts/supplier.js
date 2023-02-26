// <!-- --------------------------------------------AJAX FOR  GET SUPPLIER ADDRESS-------------------- -->

<script>
    $(document).ready(function(){
        function loaddata(type,address){
                $.ajax({
                            
                        url: "fetch_product.php",
                        type: "POST",
                        data:{
                            type : type,
                            id : address
                              },
                           success:function(data){
                            if(type=="statedata"){
                             $('#s_address').html(data);
                             }else{
                            $('#s_supplier').append(data);
                      }
                    }
                });
          }
                loaddata();

              $("#s_supplier").on("change",function(){
               var supplier = $("#s_supplier").val();
              loaddata("statedata",supplier)
            })

    });
</script>