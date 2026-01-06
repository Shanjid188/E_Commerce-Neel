from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

CATEGORY_CHOICES=(
    ('CR','Wedding'),
    ('ML','Reception'),
    ('LS','Birthday'),
    ('MS','Jamai Bou'),
    ('PN','Office Ferwell'),
    ('GH','Office Party'),
    ('CZ','Ghorar Gari'),
    ('IC','All Events Pakage'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    Product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) # type: ignore
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    Product_image = models.ImageField(upload_to='product')
    #state = models.CharField(choices=STATE_CHOICES,max_length=50)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title} ({self.quantity})"

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def total_cost(self):
        return self.quantity * self.product.discounted_price