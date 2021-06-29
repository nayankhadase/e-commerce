from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home,name='home'),
    path('signup',views.Signup,name='signup'),
    path('returncurrent',views.Returncurrent,name='returncurrent'),
    
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('category/<int:catid>/<int:subid>',views.CategoryName,name='category'),
    path('filterproducts',views.Filterproducts,name='filterproducts'),
    path('getauthorfilter',views.Getauthorfilter,name='getauthorfilter'),

    path('about',views.About,name='about'),
    path('contact',views.Contact,name='contact'),
    path('moredetails/<int:sid>',views.MoreDetails,name='moredetails'),
    
    path('search',views.Search,name='search'),


    path('addtocart/<int:pid>/<int:uid>',views.AddtoCart,name='addtocart'),
    path('showcart',views.Showcart,name='showcart'),
    path('delcart/<int:pid>/<int:uid>',views.Delcart,name='delcart'),
    path('productqty',views.Productqty,name='productqty'),
    

    path('buynow/<int:pid>/<int:uid>',views.Buynowprod,name='buynow'),
    path('buynowroductqty',views.Buynowroductqty,name='buynowroductqty'),

    path('checkout',views.Checkout,name='checkout'),
    path('cartchkout',views.Cartchkout,name='cartchkout'),
    path('orders/<int:uid>',views.Showorders,name='orders'),

    path('wishlist/<int:pid>/<int:uid>',views.Wishlists,name='wishlist'),
    path('showwishlist',views.Showwishlist,name='showwishlist'),
    path('delwishlist/<int:pid>/<int:uid>',views.Delwishlists,name='delwishlist'),

    path('checkbox',views.Filtercheck,name='checkbox'),
    path('getfilterdata',views.Getfilterdata,name='getfilterdata'),

    path('profile',views.Profile,name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)