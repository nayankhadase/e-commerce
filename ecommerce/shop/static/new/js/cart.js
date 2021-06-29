$(document).ready(
    function () {
                
                var prodlen = $('.prod')
                var qtyy = $(".qtys");  // give objects
                var pdiscc = $(".pdisc");
                var ppricee = $(".pprice");
                var delii = $(".deli");
                var pricearray = new Array();
                var mainprice = new Array();
                for( var i=0; i<prodlen.length;i++)
                {
                    var qty=qtyy[i].value;
                    var pdisc= pdiscc[i].value;
                    var pprice = ppricee[i].value;
                    var deli = delii[i].value;
                    var discount = qty * (pprice - pdisc);
                    var finalprice = (qty * pprice);
                    
                    var total = parseFloat(finalprice) - parseFloat(discount) ;
                   
                    pricearray.push(total)
                    mainprice.push(finalprice)
                }
                
                var finarr= 0;
                var mainpricesum=0;
                for( var i=0; i<(prodlen.length);i++)
                {
                    var arrdata=pricearray[i];
                    finarr+=parseFloat(arrdata);

                    var mainpriceval=mainprice[i];
                    mainpricesum+=parseFloat(mainpriceval);  
                }
                var delip
                if (mainpricesum >= 299) {
                    deli = 0;
                    delip = "FREE";
                }
                else {
                    deli = 20;
                    delip = "&#8377;" + parseFloat(deli);
                }
                var lastfinal=parseFloat(finarr) + parseFloat(deli)
                
                $("#dprice").text(mainpricesum);
                $("#doff").text(mainpricesum - parseFloat(finarr));
                $("#dcharg").html(delip);
                $("#fprice").text(lastfinal);
            


        $("#removeprod").click(
            function () {
                return confirm("Do yuo want to remove it ??");

            }
        )
        $(".qtys").change(
            function (e) {
                // alert($(".cid").val())
                e.preventDefault();
                $.ajax(
                    {
                        type: "POST",
                        url: 'productqty',
                        data: {
                            pqty: $(".qtys").val(),
                            cid: $(".cid").val(),
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                        },
                        success: function (res) {
                            
                        }
                    }
                )
                var prodlen = $('.prod')
                var qtyy = $(".qtys");  // give objects
                var pdiscc = $(".pdisc");
                var ppricee = $(".pprice");
                var delii = $(".deli");
                var pricearray = new Array();
                var mainprice = new Array();
                for( var i=0; i<prodlen.length;i++)
                {
                    var qty=qtyy[i].value;
                    var pdisc= pdiscc[i].value;
                    var pprice = ppricee[i].value;
                    var deli = delii[i].value;
                    var discount = qty * (pprice - pdisc);
                    var finalprice = (qty * pprice);
                    
                    var total = parseFloat(finalprice) - parseFloat(discount) ;
                   
                    pricearray.push(total)
                    mainprice.push(finalprice)
                }
                
                var finarr= 0;
                var mainpricesum=0;
                for( var i=0; i<(prodlen.length);i++)
                {
                    var arrdata=pricearray[i];
                    finarr+=parseFloat(arrdata);

                    var mainpriceval=mainprice[i];
                    mainpricesum+=parseFloat(mainpriceval);  
                }
                var delip
                if (mainpricesum >= 299) {
                    deli = 0;
                    delip = "FREE";
                }
                else {
                    deli = 20;
                    delip = "&#8377;" + parseFloat(deli);
                }
                var lastfinal=parseFloat(finarr) + parseFloat(deli)
                
                $("#dprice").text(mainpricesum);
                $("#doff").text(mainpricesum - parseFloat(finarr));
                $("#dcharg").html(delip);
                $("#fprice").text(lastfinal);
            }
            
        )


        var cartitems = $('.product_id');
        var itemqty = $(".qtys");
        var objcartitems=new Array();
        var objcartitemsqty=new Array();
        for( var i=0; i<prodlen.length;i++)
        {
            var citem=cartitems[i].value;
            var citemqty=itemqty[i].value;
            objcartitems.push(citem)
            objcartitemsqty.push(citemqty)
        }
        $("#chkout").click(
            function (f) {
                f.preventDefault();
                $.ajax(
                    
                    {
                        type: "POST",
                        url: '/cartchkout',
                        data: {
                            'cartitems': objcartitems,
                            'cartitemsqty': objcartitemsqty,
                            price:lastfinal,
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                        },
                        success: function (res) {
                            $("#resultmodel").html(res);
                        }
                    }
                )

                }
                
            
                )
            
    }
)

