$(document).ready(function() {
    $(".ajaxLoader").hide();
    
    var _filterObj = {};
    var _minPrice = $('#minamount').val();
    var _maxPrice = $('#maxamount').val();
    _filterObj.minPrice = _minPrice;
    _filterObj.maxPrice = _maxPrice;

});