from django.contrib import admin
from . models import Product

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_displayc = ['id','title','discounted_price','category','Product_image']