$(document).ready(
    function () {
                var qty = $("#qtyselect").val();
                var pdisc = parseInt($("#pdisc").text());
                var pprice = parseInt($("#pprice").text());
                var deli = parseInt($("#deli").text());
                var discount = qty * (pprice - pdisc);
                var finalprice = (qty * pprice);
                var delip
                if (finalprice >= 299) {
                    deli = 0;
                    delip = "FREE";
                }
                else {
                    deli = 20;
                    delip = "&#8377;" + deli;
                }
                var total = finalprice - discount + deli;
                $("#dprice").text(qty * pprice);
                $("#doff").text(discount);
                $("#dcharg").html(delip);
                $("#fprice").text(total);
                $("#finprice").val(total);
            


        $("#removeprod").click(
            function () {
                return confirm("Do yuo want to remove it ??");

            }
        )
        $("#qtyselect").change(
            function (e) {
                e.preventDefault();
                $.ajax(
                    {
                        type: "POST",
                        url: '/buynowroductqty',
                        data: {
                            pqty: $("#qtyselect").val(),
                            cid: $("#cid").val(),
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                        },
                        success: function (res) {
                            
                        }
                    }
                )
                var qty = $("#qtyselect").val();
                var pdisc = parseInt($("#pdisc").text());
                var pprice = parseInt($("#pprice").text());
                var deli = parseInt($("#deli").text());
                var discount = qty * (pprice - pdisc);
                var finalprice = (qty * pprice);
                var delip
                if (finalprice >= 299) {
                    deli = 0;
                    delip = "FREE";
                }
                else {
                    deli = 20;
                    delip = "&#8377;" +deli;
                }
                var total = finalprice - discount + deli;
                $("#dprice").text(qty * pprice);
                $("#doff").text(discount);
                $("#dcharg").html(delip);
                $("#fprice").text(total);
                $("#finprice").val(total);
            }
            
        )
        var addr=$("#address").text()
        
        $("#chkout").click(
            function (f) {

                var option = confirm("your delivery address: " + addr)
                
                if (option == false)
                {
                    alert("Please enter your Delivery address to proceed")
                }
                else{
                    f.preventDefault();
                    $.ajax(
                        {
                            type: "POST",
                            url: '/checkout',
                            data: {
                                pqty: $("#qtyselect").val(),
                                uid: $("#uid").val(),
                                pid: $("#pid").val(),
                                price:$("#finprice").val(),
                                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                            },
                            success: function (res) {
                                $("#resultmodel").html(res);
                            }
                        }
                    )  
                }
                

                }
            )

    })

