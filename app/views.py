from datetime import timezone
from django.db.models import Count
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from . forms import CustomerRegistrationFrom, CustomerProfileForm
from . models import Customer, Product, Cart, OrderPlaced
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Value
from django.db.models.functions import Lower
 
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "app/home.html", {'products': products})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationFrom()
        return render(request,"app/customerregistration.html",locals())
    def post(self,request):
        form = CustomerRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Registration Successfull")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"app/customerregistration.html",locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,"app/profile.html",locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
                user = request.user
                name = form.cleaned_data['name']
                locality = form.cleaned_data['locality']
                city = form.cleaned_data['city']
                mobile = form.cleaned_data['mobile']
                zipcode = form.cleaned_data['zipcode']

                reg =Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode)
                reg.save()
                messages.success(request,"Congratulations! Profile Save Successfuly")
            
        else:
             messages.warning(request,"Invalid Input Data")
            
        return render(request,"app/profile.html",locals())   
    
# def add_to_cart(request, id):
#     product = get_object_or_404(Product, id=id)
#     cart_item, created = Cart.objects.get_or_create(user=request.user,product=product)
#     if not created:
#         cart_item.quantity = 1
#         cart_item.save()
#     return redirect('show_cart') 

def search_products(request):
    query = request.GET.get('q')
    if query:
        # Normalize the query by removing spaces and converting to lowercase
        normalized_query = query.replace(" ", "").lower()
        
        # Filter products by normalizing the title in the same way
        product_results = Product.objects.annotate(normalized_title=Lower('title')).filter(normalized_title__contains=normalized_query).annotate(item_type=Value(value='home'))
        
        search_results = list(product_results)
    else:
        search_results = None
        
    return render(request, 'app/search_results.html', context={'search_results': search_results, 'query': query})

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        messages.info(request, f"'{product.title}' is already in your cart.")
    else:
        messages.success(request, f"'{product.title}' added to your cart successfully.")
    return redirect(request.META.get('HTTP_REFERER', 'show_cart'))

def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_amount = sum(item.total_cost for item in cart_items)
    context = {'cart_items': cart_items,'total_amount': total_amount}
    return render(request, 'app/show_cart.html', context = context)            

def remove_from_cart(request, id):
    try:
        cart_item = Cart.objects.get(id=id, user=request.user)
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")
    except Cart.DoesNotExist:
        messages.warning(request, "Item not found in your cart.")
    return redirect('show_cart')

def update_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    new_quantity = request.POST.get('quantity')

    try:
        new_quantity = int(new_quantity)
        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()
            messages.success(request, "Cart updated successfully.")
        else:
            messages.warning(request, "Quantity must be at least 1.")
    except ValueError:
        messages.error(request, "Invalid quantity.")

    return redirect('show_cart')

def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        messages.warning(request, "Your cart is empty.")
        return redirect('show_cart')
    for item in cart_items:
        OrderPlaced.objects.create(user=request.user,product=item.product,quantity=item.quantity)
        item.delete()
    messages.success(request, "Your order has been placed successfully!")
    return redirect('orders')

def orders(request):
    orders = OrderPlaced.objects.filter(user=request.user).order_by('-ordered_date')
    return render(request, 'app/orders.html', {'orders': orders})


def chatbot(request):
    return render(request, 'app/gemini.html')