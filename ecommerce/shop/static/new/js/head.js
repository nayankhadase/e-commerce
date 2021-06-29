$(document).ready(
function()
    {
        $("#searchbtn").click(
        function()
            {
                var heigh=$("#navbar").css('height');
                $("#search").css('top',heigh);
                $("#search").toggleClass("d-none");  
            }
        )
    }
)