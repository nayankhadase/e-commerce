$(document).ready(
    function () {
        // FOR WISHLIST HEART
        $("#addwish").click(
            function () {
                $(this).toggleClass("d-none");
            }
        )

        $("#delwish").click(
            function () {
                $(this).toggleClass("d-none");
            }
        )
        // FOR FILTER PRODUCT
        $("#prodfilter").change(
            function(e){
                e.preventDefault();
                $.ajax(
                    {
                        url:'/filterproducts',
                        data:{
                            filterprod:$("#prodfilter").val(),
                            catid:$("#catid").val(),
                            subid:$("#subid").val(),
                        },
                        success:function(res){
                            $("#filterprod").html(res);
                        }
                    }
                )
            }
        )
            // FOR FILTER BY AUTHOR
        $('input').click(
            function(){
                var newarry = new Array();
                var chk=$('input');
                for(var i=0;i < chk.length;i++)
                {
                    if (chk[i].checked)
                    {
                        newarry.push(chk[i].value);
                    }
                    
                }
                console.log(newarry);
                $.ajax({
                    type:'POST',
                    url:'/getauthorfilter',
                    data:{
                        chkval:newarry,
                        catid:$("#catid").val(),
                        subid:$("#subid").val(),
                        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(result){
                        $("#filterprod").html(result);
                    }
                    
                })
            }
        )

        


    }
)
