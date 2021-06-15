from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import django.utils.safestring as safestring
from django.core.validators import MinLengthValidator
import datetime

# Create your models here.
class loaisanpham(models.Model):
    l_ten = models.CharField(max_length=100)
    active = models.BooleanField("Is Active", default=True)

    def __str__(self):
        return self.l_ten

class sanpham(models.Model):
    l_id = models.ForeignKey(loaisanpham, on_delete=models.CASCADE)
    sp_ten = models.CharField("Ten san pham", max_length=200)
    sp_gia = models.IntegerField("Gia", default=0)
    sp_soluong = models.IntegerField("So luong", default=0)
    sp_hinhanh = models.ImageField("Hinh anh",upload_to='uploads/%Y/%m/%d/')
    sp_mota = models.TextField("Mo ta")            

    def image_tag(self):
        if self.image:
            return safestring.mark_safe('<img src="%s%s" width="200" height="200" />' % (settings.MEDIA_URL, self.image))
        else:
            return ""

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
    def __str__(self):
        return self.sp_ten   
        
    @staticmethod
    def get_products_by_id(ids):
        return sanpham.objects.filter(id__in =ids)

class khachhang(models.Model):
    kh_ten = models.CharField(max_length=50)
    kh_sdt = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    #login
    def get_customer_by_email(email):
        try:
            return khachhang.objects.get(email=email)
        except:
            return False

    def __str__(self):
        return self.kh_ten

#xác thực email
    def isExists(self):
        if khachhang.objects.filter(email = self.email):
            return True

        return False

class donhang(models.Model):
    kh = models.ForeignKey(khachhang, on_delete=models.CASCADE, null=True)
    diachi = models.CharField(max_length=50, default='', blank=True)
    sdt = models.CharField(max_length=50, default='', blank=True)
    ngay = models.DateField(default=datetime.datetime.today)
    trangthai = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(kh_id):
        return donhang.objects.filter(khachhang=kh_id).order_by('-date')
    

class chitietdonhang(models.Model):
    sp = models.ForeignKey(sanpham, on_delete=models.CASCADE, null=True)
    dh = models.ForeignKey(donhang, on_delete=models.CASCADE, null=True)
    ct_soluong = models.IntegerField(default=1)
    ct_dongia = models.IntegerField(default=0)
        