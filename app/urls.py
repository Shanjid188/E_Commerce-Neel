from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from  .forms import LoginForm, MyPasswordResetForm

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="category"),
    path("category-title/<val>", views.CategoryView.as_view(),name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    path("profile/", views.ProfileView.as_view(),name="profile"),
    path("show_cart/", views.show_cart, name="show_cart"),
    path("add_cart/<str:id>/",views.add_to_cart, name="add_to_cart"),
    path("delete_products/<str:id>/",views.remove_from_cart, name='remove_from_cart'),
    path("update_cart/<str:id>/", views.update_cart, name="update_cart"),
    path("order_list/", views.orders, name = "orders"),
    path("checkout/",views.checkout, name="checkout"),

    path('chatbot/', views.chatbot, name='chatbot'),
    path('search_products/', views.search_products, name='search_products'),
    
    #Login Authentication
    path("registration/", views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name="login"),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name="password_reset"),
    path('logout/', views.logout_user, name="logout")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   