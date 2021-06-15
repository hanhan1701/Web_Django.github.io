from __future__ import unicode_literals
from django.core.checks.messages import Error
from django.contrib.auth.hashers import make_password, check_password #hash password
from django.template.loader import render_to_string, get_template
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from banhang.models import loaisanpham, sanpham, khachhang, donhang, chitietdonhang
from .forms import RegistrationForm
from django.views import View
# Create your views here.
# def index(request):
#     return render(request,'home/index.html')

# Trang chu
class index(View):
    def post(self, request):
        product= request.POST.get('product')
        remove = request.POST.get('remove')
        cart= request.session.get('cart')

        if cart:
            dh_soluong=cart.get(product)
            if dh_soluong:
                if remove:
                    if dh_soluong<=1:
                        cart.pop(product)
                    else:    
                        cart[product]=dh_soluong - 1
                elif sanpham.objects.get(id__in =str(product)).sp_soluong > dh_soluong:
                    cart[product]=dh_soluong + 1 
            else:
                cart[product]= 1    
        else: 
            cart={}
            cart[product]=1
        request.session['cart'] = cart 

        return redirect('trangchu')

    def get(self, request):
        cart =request.session.get('cart')
        if not cart:
            request.session.cart = {}
        loai_objs = loaisanpham.objects.filter(active__exact=True)
        featureItems = sanpham.objects.filter()
        context = {
            'loai_objs': loai_objs,
            'featureItems' : featureItems,
        }
   
        return render(request, "home/index.html", context)  

#Danh sach san pham
def product(request):
    loai_objs = loaisanpham.objects.filter(active__exact=True)
    featureItems = sanpham.objects.filter()
    context = {
        'loai_objs': loai_objs,
        'featureItems' : featureItems,
    }
    return render(request,'home/product.html',context)  

# Danh sach san pham theo loai
def productcat(request,sp_id):
    loai_objs = loaisanpham.objects.filter(active__exact=True)
    productcat = sanpham.objects.filter(l_id=sp_id)
    context = {
        'loai_objs': loai_objs,
        'productcat' : productcat,
    }
    return render(request,'home/productcate.html',context)  

# chi tiet san pham
def chitietsp(request,sanpham_id):
    loai_objs = loaisanpham.objects.filter(active__exact=True)
    detail =sanpham.objects.get(id=sanpham_id)
    context={
        'loai_objs': loai_objs,
       'detail': detail,
   }
    return render(request, 'home/detail.html',context)

  
# Dang ki
#Xac thuc khach hang
def validateCustomer(kh_khachhang):
    error_message=None
    if(not kh_khachhang.kh_ten):
        error_message= "Họ tên không bỏ trống!"
    elif len(kh_khachhang.kh_ten)<4:
        error_message = 'Họ tên phải dài hơn 4 ký tự hoặc hơn' 
    elif(not kh_khachhang.kh_sdt):
        error_message= "Số điện thoại không bỏ trống!"
    elif len(kh_khachhang.kh_sdt)<10:
        error_message = 'Số điện thoại dài hơn 10 ký tự' 
    elif len(kh_khachhang.password)<3:
        error_message = 'Mật khẩu phải dài hơn 3 ký tự hoặc hơn' 
    elif len(kh_khachhang.email)<5:
        error_message = 'Họ tên phải dài hơn 4 ký tự hoặc hơn' 
    elif kh_khachhang.isExists():
        error_message = 'Email đã tồn tại'
    return error_message    

#hàm đăng kí
def registerUser(request):
    postData = request.POST
    kh_ten = postData.get('name')
    kh_sdt = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')
    # validation
    value ={
        'kh_ten':kh_ten,
        'kh_sdt':kh_sdt,
        'email':email
    }
        
    error_message = None
    kh_khachhang = khachhang(kh_ten=kh_ten,kh_sdt=kh_sdt, email=email, password=password)
    error_message =validateCustomer(kh_khachhang)
      
    #saving
    if not error_message:
        kh_khachhang.password=make_password(kh_khachhang.password)#hash password
        kh_khachhang.register()
        return redirect('dangnhap')
    else:    
        data={
            'error':error_message,
            'values':value
        }
        return render(request,'home/signup.html',data)

def signup(request):
    if request.method =='GET':
        return render(request,'home/signup.html' )
    else:
        return registerUser(request)

#đăng nhập
def login(request):
    if request.method=='GET':
        return render(request,'home/login.html') 
    else:
        email= request.POST.get('email')
        password= request.POST.get('password')
        kh_khachhang=khachhang.get_customer_by_email(email)
        error_message = None
        if kh_khachhang:
            flag= check_password(password,kh_khachhang.password)
            if flag:
                request.session['kh_khachhang']= kh_khachhang.id
                return redirect('trangchu')
            else:
                error_message = 'Email hoặc mật khẩu không hợp lệ!'
        else:
            error_message = 'Email hoặc mật khẩu không hợp lệ!'         
        return render(request,'home/login.html',{'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('dangnhap')        

#giỏ hàng
class cart(View):
    def get(self, request):
        if request.session.get('cart') is None:
            request.session['cart'] = {}

        ids = list(request.session.get('cart').keys())
        products = sanpham.get_products_by_id(ids)
        loai_objs = loaisanpham.objects.filter(active__exact=True)
        return render(request , 'home/cart.html' , { 'products' : products, 'loai_objs':loai_objs } )
    
    def post(self, request):
        del request.session['cart'][request.POST['productId']]  #xóa sp giỏ hàng
        request.session['cart'] = request.session['cart']

        ids = list(request.session.get('cart').keys())
        products = sanpham.get_products_by_id(ids)
        return render(request , 'home/cart.html' , {'products' : products} )


#Thanh toán    
def checkout(request):
    diachi = request.POST.get('address')
    sdt = request.POST.get('phone')
    kh = request.session.get['kh_khachhang']
    cart = request.session.get('cart')
    products = sanpham.get_products_by_id(list(cart.keys()))


    if not kh:
        return redirect('dangnhap')

    new_dh = donhang(
        kh=khachhang(id=kh),
        diachi=diachi,
        sdt=sdt
    )

    new_dh.save()
    
    for product in products:
        order = chitietdonhang(
            dh=new_dh,
            sp=product,
            ct_dongia=product.sp_gia,
            ct_soluong=cart.get(str(product.id))
        )

        # tru so luong san pham khi dat hang
        sp_tmp = sanpham.objects.get(id__in =str(product.id))
        sp_tmp.sp_soluong -= order.ct_soluong
        sp_tmp.save()

        order.save() 

    request.session['cart'] = {}

    return redirect('giohang') 
   