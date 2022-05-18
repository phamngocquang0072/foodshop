$(document).ready(function(){
    //add to cart

   $(document).on('click','#addToCart', function (){
       var _vm=$(this);
       var _qty=parseInt($("#qty").val());
       var _proId=$(".product-id").val();
       var _proTitle=$(".product-title").val();
    //    var _proImage=$(".product__details__pic__item--large").val();
       var _proPrice=parseFloat($(".product__details__price").text().replace('$', ''));
       console.log(_qty, _proId, _proTitle, _proPrice);
       //ajax 
       $.ajax({
           url:'/add-to-cart',
           data:{
               'id':_proId,
               'qty':_qty,
               'title':_proTitle,
            //    'image': _proImage,
               'price':_proPrice,
           },
           dataType:'json',
           beforeSend:function(){
               _vm.attr('disabled',true);
           },
           success:function(res){
               console.log(res);
               $('.cart-list-total').text(res.total);
               _vm.attr('disabled',false);
                
           }
       });


   });
   //end add to cart


});