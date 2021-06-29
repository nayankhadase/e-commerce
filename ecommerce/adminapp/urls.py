from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Loginpage,name='pagelogin'),
    path('loginuser',views.Login_user),

    path('dashbord',views.Dashbord,name='dashbord'),
    path('logout',views.Logout,name='log_out'),

    path('addcategory',views.Addcategory,name='addcategory'),
    path('uploadcategory',views.Uploadcategory,name='uploadcategory'),
    path('showcategory',views.Showcategory,name='showcategory'),
    path('statuscategory/<int:sid>/<str:cat_status>',views.StatusCategory,name='statuscategory'),
    path('deletecategory/<int:sid>',views.Deletecategory,name='deletecategory'),
    path('editcategory/<int:sid>',views.Editcategory,name='editcategory'),
    path('updatecategory/<int:sid>',views.Updatecategory,name='updatecategory'),

    path('showsubcategory',views.ShowSubCategory,name='showsubcategory'),
    path('addsubcategory',views.AddSubCategory,name='addsubcategory'),
    path('uploadsubcategory',views.UploadSubCategory,name='uploadsubcategory'),
    path('subcategorystatus/<int:sid>/<str:subcat_status>',views.SubCategoryStatus,name='subcategorystatus'),
    path('subcategorydelete/<int:sid>',views.SubCategoryDelete,name='subcategorydelete'),
    path('editsubcategory/<int:sid>',views.EditSubCategory,name='editsubcategory'),
    path('updatesubcategory/<int:sid>',views.UpdateSubCategory,name='updatesubcategory'),

    path('showproduct',views.ShowProduct,name='showproduct'),
    path('addproduct',views.AddProduct,name='addproduct'),

    path('fetchsubcat',views.Fetchsubcat,name='fetchsubcat'),
    # path('fetcheditsubcat',views.Fetcheditsubcat,name='fetcheditsubcat'),

    path('uploadproduct',views.UploadProduct,name='uploadproduct'),
    path('deleteproduct/<int:sid>',views.DeleteProduct,name='deleteproduct'),
    path('editproduct/<int:sid>',views.EditProduct,name='editproduct'),
    path('updateproduct/<int:sid>',views.UpdateProduct,name='updateproduct'),
    path('productstatus/<int:sid>/<str:prod_status>',views.ProductStatus,name='productstatus'),

    path('manageuser',views.ManageUser,name='manageuser'),
    path('deleteuser/<int:sid>',views.DeletUser,name='deleteuser'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)