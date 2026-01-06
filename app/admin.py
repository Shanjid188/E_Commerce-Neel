from django.contrib import admin
from . models import Customer, Product, OrderPlaced, Cart

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','Product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','zipcode']

@admin.register(OrderPlaced)
class OrderPlaced(admin.ModelAdmin):
    list_display = ['id','user','product','quantity','ordered_date']

    