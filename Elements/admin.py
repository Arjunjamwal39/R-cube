from django.contrib import admin
from .models import Product, Customer, Cart, OrderStatus, UserOTP, Deliveryboy, practice

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','price', 'category']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','Contact_number','locality','city', 'zipcode','state', 'address_type']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderStatus)
class OrderstatusModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date',
    'status']

@admin.register(practice)
class practiceModelAdmin(admin.ModelAdmin):
    list_display = ['title','discription','imagee']

@admin.register(UserOTP)
class practiceModelAdmin(admin.ModelAdmin):
    list_display = ['user','time_st','otp']

@admin.register(Deliveryboy)
class deliveryModelAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Contact_number','discription','emaill']