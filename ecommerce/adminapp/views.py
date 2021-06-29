from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Category,SubCategory,Product
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from shop.models import Userdata
# Create your views here.

def Loginpage(request):
    return render(request,'page-login.html')

def Dashbord(request):
    if request.user.is_authenticated:
        return render(request,'dashbord.html')
    else:
        return HttpResponse("404 error..")

# admin login
def Login_user(request):
    if request.method == "POST":
        vusername=request.POST.get('username')
        vpassword=request.POST.get('password')
        log_user=auth.authenticate(username=vusername,password=vpassword)
        if log_user is not None:
            auth.login(request,log_user)
            return redirect('/adminapp/dashbord')
        else:
            messages.info(request,"username or password is in correct")
            return redirect('/adminapp')
    else:
        return HttpResponse("404 error..")


def Logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('/adminapp')
    else:
        return HttpResponse("404 error..")


# category page
def Addcategory(request):
    if request.user.is_authenticated:
        return render(request,'add_category.html')
    else:
        return HttpResponse("404 error..")

def Uploadcategory(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            vcategory=request.POST.get('hcategory')
            objcategory=Category()
            objcategory.category=vcategory
            objcategory.save()
            return redirect('/adminapp/showcategory')
    else:
        return HttpResponse("404 error..")

def Showcategory(request):
    if request.user.is_authenticated:
        objcategory=Category.objects.all()
        objpage=Paginator(objcategory,5)
        vpage=request.GET.get('page')
        objcategory=objpage.get_page(vpage)
        return render(request,'showcategory.html',{'category':objcategory})
    else:
        return HttpResponse("404 error..")

def StatusCategory(request,sid,cat_status):
    if request.user.is_authenticated:
        if cat_status == "BLOCK":
            objcategory=Category.objects.get(id=sid)
            objcategory.cat_status="UNBLOCK"
            objcategory.save()
            return redirect('/adminapp/showcategory')
        else:
            objcategory=Category.objects.get(id=sid)
            objcategory.cat_status="BLOCK"
            objcategory.save()
            return redirect('/adminapp/showcategory')
    else:
        return HttpResponse("404 error..")


def Deletecategory(request,sid):
    if request.user.is_authenticated:
        objcategory=Category.objects.get(id=sid)
        objcategory.delete()
        return redirect('/adminapp/showcategory')
    else:
        return HttpResponse("404 error..")

def Editcategory(request,sid):
    if request.user.is_authenticated:
        objcategory=Category.objects.get(id=sid)
        return render(request,'editcategory.html',{'category':objcategory})
    else:
        return HttpResponse("404 error..")

def Updatecategory(request,sid):
    if request.user.is_authenticated:
        if request.method == "POST":
            objcategory=Category.objects.get(id=sid)
            vcategory=request.POST.get('hcategory')
            objcategory.category=vcategory
            objcategory.save()
            return redirect('/adminapp/showcategory')
        else:
            return HttpResponse("404 error..")
    else:
        return HttpResponse("404 error..")

# # subcategory
def ShowSubCategory(request):
    if request.user.is_authenticated:
        objsubcategory=SubCategory.objects.raw('select * from adminapp_subcategory LEFT JOIN adminapp_category on adminapp_subcategory.categoryint = adminapp_category.id')
        objpage=Paginator(objsubcategory,5)
        vpage=request.GET.get('page')
        objsubcategory=objpage.get_page(vpage)
        
        return render(request,'showsubcategory.html',{'subcategory':objsubcategory})
    else:
        return HttpResponse("404 error..")

def AddSubCategory(request):
    if request.user.is_authenticated:
        objcategory=Category.objects.all()
        return render(request,'addsubcategory.html',{'categoryname':objcategory})
    else:
        return HttpResponse("404 error..")

def UploadSubCategory(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            vselectedcategory=request.POST.get('selectedcategory')
            vsubcategory = request.POST.get('hsubcategory')
            objsubcategory=SubCategory()
            objsubcategory.subcategory=vsubcategory
            objsubcategory.categoryint=vselectedcategory
            objsubcategory.save()
            return redirect('/adminapp/showsubcategory')
        else:
            return HttpResponse("404 error..")
    else:
        return HttpResponse("404 error..")
    
def SubCategoryStatus(request,sid,subcat_status):
    if request.user.is_authenticated:
        if subcat_status == "BLOCK":
            objsubcategory=SubCategory.objects.get(id=sid)
            objsubcategory.subcat_status="UNBLOCK"
            objsubcategory.save()
            return redirect('/adminapp/showsubcategory')
        else:
            objsubcategory=SubCategory.objects.get(id=sid)
            objsubcategory.subcat_status="BLOCK"
            objsubcategory.save()
            return redirect('/adminapp/showsubcategory')
    else:
        return HttpResponse("404 error..")


def SubCategoryDelete(request,sid):
    if request.user.is_authenticated:
        objsubcategory=SubCategory.objects.get(id=sid)
        objsubcategory.delete()
        return redirect('/adminapp/showsubcategory')
    else:
        return HttpResponse("404 error..")

def EditSubCategory(request,sid):
    if request.user.is_authenticated:
        objsubcategory=SubCategory.objects.get(id=sid)
        objcategory=Category.objects.all()
        return render(request,'editsubcategory.html',{'subcategory':objsubcategory,'category':objcategory})
    else:
        return HttpResponse("404 error..")

def UpdateSubCategory(request,sid):
    if request.user.is_authenticated:
        if request.method == "POST":
            objsubcategory=SubCategory.objects.get(id=sid)
            vselectedcategory=request.POST.get('selectedcategory')
            vsubcategory = request.POST.get('hsubcategory')
            objsubcategory.subcategory=vsubcategory
            objsubcategory.categoryint=vselectedcategory
            objsubcategory.save()
            return redirect('/adminapp/showsubcategory')
        else:
            return HttpResponse("404 error..")
    else:
        return HttpResponse("404 error..")        

# # products
def ShowProduct(request):
    if request.user.is_authenticated:
        objproduct=Product.objects.raw('select * from adminapp_product LEFT JOIN adminapp_category on adminapp_product.categoryindex = adminapp_category.id LEFT JOIN adminapp_subcategory on adminapp_product.subcategoryindex = adminapp_subcategory.id')

        # objpage=Paginator(objproduct,8)
        # vpage=request.GET.get('page')
        # objproduct=objpage.get_page(vpage)

        return render(request,'showproduct.html',{'product':objproduct})
    else:
        return HttpResponse("404 error..") 

def AddProduct(request):
    if request.user.is_authenticated:
        objsubcategory=SubCategory.objects.all()
        objcategory=Category.objects.all()
        data = {'subcategory':objsubcategory,'category':objcategory}
        return render(request,'addproduct.html',data)
    else:
        return HttpResponse("404 error..")

def Fetchsubcat(request):
    if request.user.is_authenticated:
        vcat=request.GET.get('category')
        objsubcat=SubCategory.objects.filter(categoryint=vcat)
        return render(request,'fetchsubcat.html',{'subcategory':objsubcat})
    else:
        return HttpResponse("404 error..")

def UploadProduct(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            categoryindex=request.POST.get('selectcategory')
            subcategoryindex=request.POST.get('selectsubcategory')
            productname=request.POST.get('productname')
            author=request.POST.get('author')
            productprice=request.POST.get('productprice')
            discount=request.POST.get('discount')
            discountprice=request.POST.get('discountprice')
            proddiscription=request.POST.get('proddiscription')
            uploadimg=request.FILES['prodimg']
            objproduct=Product()
            objproduct.categoryindex=categoryindex
            objproduct.subcategoryindex=subcategoryindex
            objproduct.productname=productname
            objproduct.author=author
            objproduct.productprice=productprice
            objproduct.discount=discount
            objproduct.discountprice=discountprice
            objproduct.proddiscription=proddiscription
            objproduct.productimage=uploadimg
            objproduct.save()
            return redirect('/adminapp/showproduct')
    else:
        return HttpResponse("404 error..")

def DeleteProduct(request,sid):
    if request.user.is_authenticated:
        objproduct=Product.objects.get(id=sid)
        objproduct.delete()
        return redirect('/adminapp/showproduct')
    else:
        return HttpResponse("404 error..")

def EditProduct(request,sid):
    if request.user.is_authenticated:
        objproduct=Product.objects.get(id=sid)
        objsubcategory=SubCategory.objects.all()
        objcategory=Category.objects.all()
        data = {'product':objproduct,'subcategory':objsubcategory,'category':objcategory}
        return render(request,'editproduct.html',data)
    else:
        return HttpResponse("404 error..")

# def Fetcheditsubcat(request):
#     if request.user.is_authenticated:
#         vcat=request.GET.get('category')
#         objsubcat=SubCategory.objects.filter(categoryint=vcat)
#         return render(request,'fetcheditsubcat.html',{'subcategory':objsubcat})
#     else:
#         return HttpResponse("404 error..")

def UpdateProduct(request,sid):
    if request.user.is_authenticated:
        if request.method == "POST":
            objproduct=Product.objects.get(id=sid)
            categoryindex=request.POST.get('selectcategory')
            subcategoryindex=request.POST.get('selectsubcategory')
            productname=request.POST.get('productname')
            author=request.POST.get('author')
            productprice=request.POST.get('productprice')
            discount=request.POST.get('discount')
            discountprice=request.POST.get('discountprice')
            proddiscription=request.POST.get('proddiscription')
            filevalid=request.POST.get('filevalid')

            if filevalid != "NULL":
                uploadimg=request.FILES['prodimg']
                objproduct.productimage=uploadimg
                
            objproduct.categoryindex=categoryindex
            objproduct.subcategoryindex=subcategoryindex
            objproduct.productname=productname
            objproduct.author=author
            objproduct.productprice=productprice
            objproduct.discount=discount
            objproduct.discountprice=discountprice
            objproduct.proddiscription=proddiscription
            objproduct.save()
            return redirect('/adminapp/showproduct')
    else:
        return HttpResponse("404 error..")

def ProductStatus(request,sid,prod_status):
    if request.user.is_authenticated:
        if prod_status == "BLOCK":
            objproduct=Product.objects.get(id=sid)
            objproduct.prod_status="UNBLOCK"
            objproduct.save()
            return redirect('/adminapp/showproduct')
        else:
            objproduct=Product.objects.get(id=sid)
            objproduct.prod_status="BLOCK"
            objproduct.save()
            return redirect('/adminapp/showproduct')
    else:
        return HttpResponse("404 error..")

# manage user
def ManageUser(request):
    if request.user.is_authenticated:
        objusers=Userdata.objects.all()
        return render(request,'manageuser.html',{'userdata':objusers})
    else:
        return HttpResponse("404 error..")

def DeletUser(request,sid):
    if request.user.is_authenticated:
        objuser=Userdata.objects.get(id=sid)
        objuser.delete()
        return redirect('/adminapp/manageuser')
    else:
        return HttpResponse("404 error..")


