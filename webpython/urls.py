"""webpython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index.as_view(),name="trangchu"),
    path('home/product',views.product,name="sanpham"),
    path('home/productcat/<int:sp_id>/',views.productcat,name="sanphamtheoloai"),
    path('chitietsp/<int:sanpham_id>/', views.chitietsp, name="chitietsp"),
    
    # path('home/addcart',views.addcart,name='mua hang'),
    # path('home/cart',views.cart,name='giohang'),
    path('home/cart',views.cart.as_view(),name='giohang'),
    path('checkout',views.checkout,name='dathang'),
    path('signup/',views.signup,name="dangki"), 
    path('login/',views.login,name="dangnhap"),
    path('logout/',views.logout,name="dangxuat"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
