$(document).ready(
    function () {
        $("#bsignup").click(
            function () {
                $("#bsignup").addClass('btn_indigo');
                $("#blogin").addClass('btn_outline_indigo');
                $("#blogin").removeClass('btn_indigo');
            }
        )
        $("#blogin").click(
            function () {
                $("#blogin").addClass('btn_indigo');
                $("#bsignup").addClass('btn_outline_indigo');
                $("#bsignup").removeClass('btn_indigo');
            }
        )
        
        //this is for carousel
        $(".wish-icon i").click(
            function () {
                $(this).toggleClass("fa-heart fa-heart-o");
            }
        )
        

    }
)
