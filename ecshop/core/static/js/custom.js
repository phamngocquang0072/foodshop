$(document).ready(function(){
    //add to cart

   $(document).on('click','#addToCart', function (){
       var _vm=$(this);
       var _index=_vm.attr('data-index');
       var _qty=parseInt($(".product-qty-"+_index).val());
       var _proId=$(".product-id-"+_index).val();
       var _proTitle=$(".product-title-"+_index).val();
       var _proPrice=parseFloat($(".price-"+_index).text().replace('$', ''));
       //    var _proImage=$(".product__details__pic__item--large"+_index).val();
       
       console.log(_qty, _proId, _proTitle, _proPrice, "#product-price-"+_index);
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

   // Delete item from cart

   $(document).on('click','#delete-item', function (){
        var _pId1=$(this).attr('data-item');
        var _vm=$(this);
        console.log(_pId1);
        //ajax 
        $.ajax({
            url:'/delete-cart-item',
            data:{
                'id':_pId1,

            },
            dataType:'json',
            beforeSend:function(){
                _vm.attr('disabled',true);
            },
            success:function(res){
                console.log(res);
                // $('.cart-list-total').text(res.total);
                _vm.attr('disabled',false);
                $('#cartList').html(res.data);
                
            }
        });
    });

   // End delete item from cart

   // Update quantity sub input
   $(document).on('click','#quantitysub', function () {
        var _pId1=$(this).attr('data-item');
        var _qty =$('.product-qty-'+_pId1).val();
        var _vm=$(this);
        console.log(_qty, _pId1);
        //ajax 
        $.ajax({
            url:'/update-cart-item',
            data:{
                'id':_pId1,
                'qty':_qty,
            },
            dataType:'json',
            beforeSend:function(){
                _vm.attr('disabled',true);
            },
            success:function(res){
                console.log(res);
                // $('.cart-list-total').text(res.total);
                _vm.attr('disabled',false);
                $('#cartList').html(res.data);
                
            }
        });
    });
    // End update sub quantity input

    // Update quantity add input
    $(document).on('click','#quantityadd', function () {
        var _pId1=$(this).attr('data-item');
        var _qty =$('.product-qty-'+_pId1).val();
        var _vm=$(this);
        console.log(_qty, _pId1);
        //ajax 
        $.ajax({
            url:'/update-cart-item',
            data:{
                'id':_pId1,
                'qty':_qty,
            },
            dataType:'json',
            beforeSend:function(){
                _vm.attr('disabled',true);
            },
            success:function(res){
                console.log(res);
                $('.cart-list-total').text(res.total);
                _vm.attr('disabled',false);
                $('#cartList').html(res.data);
                
            }
        });
    });
    // End update add quantity input
    


});