$('.visibility-cart').on('click', function () {

    var $btn = $(this);
    var $cart = $('.cart');
    console.log($btn);

    if ($btn.hasClass('is-open')) {
        $btn.removeClass('is-open');
        $btn.text('O')
        $cart.removeClass('is-open');
        $cart.addClass('is-closed');
        $btn.addClass('is-closed');
    } else {
        $btn.addClass('is-open');
        $btn.text('X')
        $cart.addClass('is-open');
        $cart.removeClass('is-closed');
        $btn.removeClass('is-closed');
    }


});

// SHOPPING CART PLUS OR MINUS
$('a.qty-minus').on('click', function (e) {
    
    e.preventDefault();
    var $this = $(this);
    var $input = $this.closest('div').find('input');
    var value = parseInt($input.val());
    var value = parseInt($input.val());
    var id = $this.attr('width');
    var price = $('#price'.concat(id)).text();

    if (value > 1) {
        value = value - 1;
    } else {
        value = 0;
    }
    var tprice = price * value;
    $("#totalprice".concat(id)).text(tprice);
    
    $input.val(value);

});

$('a.qty-plus').on('click', function (e) {
    e.preventDefault();
    var $this = $(this);
    var $input = $this.closest('div').find('input');
    var value = parseInt($input.val());
    var id = $this.attr('width');
    var price = $('#price'.concat(id)).text();

    if (value < 100) {
        value = value + 1;
    } else {
        value = 100;
    }
    var tprice= price*value;
    var str = "#totalprice".concat(id)
    console.log(id)
    $(str).text(tprice);
    $input.val(value);
});

// RESTRICT INPUTS TO NUMBERS ONLY WITH A MIN OF 0 AND A MAX 100
$('input').on('blur', function () {

    var input = $(this);
    var value = parseInt($(this).val());

    if (value < 0 || isNaN(value)) {
        input.val(0);
    } else if
        (value > 100) {
        input.val(100);
    }
});

$('a.qty').on('click', function (e) {
    var elms = document.querySelectorAll("[class='tprice']");
    var totalprice=0;
    for (var i = 0; i < elms.length; i++)
        totalprice=totalprice+parseInt(elms[i].innerHTML);

    $("#finaltotal").text(totalprice);
});
window.onload = function (e) {
    e.preventDefault();
    var $this = $(this);
    var $input = $this.closest('div').find('input');
    var value = parseInt($input.val());

    var elms = document.querySelectorAll("[id='duplicateID']");

    for (var i = 0; i < elms.length; i++)
        elms[i].style.display = 'none';

    var id = $this.attr('width');
    var price = $('#price'.concat(id)).text();
    var tprice = price * value;
    var str = "#totalprice".concat(id)
    console.log(id)
    $(str).text(tprice);

    var elms = document.querySelectorAll("[class='tprice']");
    var totalprice = 0;
    for (var i = 0; i < elms.length; i++)
        totalprice = totalprice + parseInt(elms[i].innerHTML);

    $("#finaltotal").text(totalprice);
    $("#ffinaltotal").text(totalprice+40);
}
$('a.submit').on('click', function (e) {
    $('#form').submit();

});
$('#radio').on('change', function (e) {
    var x=$('input[type="radio"]:checked').val("PONL");
    var y = document.querySelector('input[name="payment"]:checked').value;
    console.log(y)
    $('input[type="hidden"]').val("PONL");

});
$('#radio1').on('change', function (e) {
    var x = $('input[type="radio"]:checked').val("PCOD");
    var y = document.querySelector('input[name="payment"]:checked').value;
    console.log(y)
    $('input[type="hidden"]').val("PCOD");
    var y = document.querySelector('input[type="hidden"]').value;

});

