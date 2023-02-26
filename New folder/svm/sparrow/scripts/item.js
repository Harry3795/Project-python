// <!-- ---------------------------ajax script for  select item name and automatically comes price -->
<script>
    $(document).ready(function(){
        function loaddata(type,address){
                $.ajax({
                            
                        url: "fetch_price.php",
                        type: "POST",
                        data:{
                            type : type ,
                            id : address
                              },
                    success:function(data){
                            if(type=="statedata"){
                             $('#rate').html(data);
                             }else{
                            $('#item').append(data);
                      }
                    }
                });
          }
                loaddata();

              $("#item").on("change",function(){
               var supplier = $("#item").val();
              loaddata("statedata",supplier)
            })

    });
</script>    