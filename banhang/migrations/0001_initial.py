# Generated by Django 3.1.6 on 2021-05-12 14:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='khachhang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kh_ten', models.CharField(max_length=50)),
                ('kh_sdt', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='loaisanpham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_ten', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='sanpham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_ten', models.CharField(max_length=200, verbose_name='Ten san pham')),
                ('sp_gia', models.IntegerField(default=0, verbose_name='Gia')),
                ('sp_soluong', models.IntegerField(default=0, verbose_name='So luong')),
                ('sp_hinhanh', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Hinh anh')),
                ('sp_mota', models.TextField(verbose_name='Mo ta')),
                ('l_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banhang.loaisanpham')),
            ],
        ),
        migrations.CreateModel(
            name='donhang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dh_soluong', models.IntegerField(default=1)),
                ('dh_gia', models.IntegerField()),
                ('diachi', models.CharField(blank=True, default='', max_length=50)),
                ('sdt', models.CharField(blank=True, default='', max_length=50)),
                ('ngay', models.DateField(default=datetime.datetime.today)),
                ('trangthai', models.BooleanField(default=False)),
                ('kh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banhang.khachhang')),
                ('sp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banhang.sanpham')),
            ],
        ),
        migrations.CreateModel(
            name='donhang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banhang.sanpham')),
                ('dh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banhang.donhang')),
                ('ct_soluong', models.IntegerField(default=1)),
                ('ct_dongia', models.IntegerField(default=0)),
            ],
        )
    ]
