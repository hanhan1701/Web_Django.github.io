from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import chitietdonhang, loaisanpham
from .models import sanpham
from .models import khachhang
from .models import donhang
from .models import chitietdonhang

# Register your models here.
class loaisanphamAdmin(admin.ModelAdmin):
    list_display = ['id', 'l_ten']
    list_filter = ['active']
    search_fields = ['l_ten']
admin.site.register(loaisanpham, loaisanphamAdmin)

class sanphamAdmin(admin.ModelAdmin):
    list_display = ['id', 'sp_ten','sp_gia','sp_soluong','sp_hinhanh','sp_mota','l_id']
    list_filter = ['sp_gia']
    search_fields = ['sp_ten']
    readonly_fields = ['image_tag'] 
admin.site.register(sanpham, sanphamAdmin)

class khachhangAdmin(admin.ModelAdmin):
    list_display = ['id', 'kh_ten','kh_sdt','email','password']
    list_filter = ['kh_ten']
    search_fields = ['kh_ten']
admin.site.register(khachhang,khachhangAdmin)

class donhangAdmin(admin.ModelAdmin):
    list_display = ['id','kh','diachi','sdt','ngay','trangthai']
    search_fields = ['kh']
    list_filter = (
        ('ngay', DateRangeFilter),
        'kh'
    )
admin.site.register(donhang,donhangAdmin)

class chitietdonhangAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/hehe.js',)
        
    list_display = ['id', 'id_sp', 'sp','dh', 'ngay', 'ct_soluong', 'ct_dongia']
    search_fields = ['dh']
    list_filter = (
        ('dh__ngay', DateRangeFilter),
    )

    def id_sp(self, obj):
        return obj.sp.id

    def ngay(self, obj):
        return obj.dh.ngay

admin.site.register(chitietdonhang,chitietdonhangAdmin)

