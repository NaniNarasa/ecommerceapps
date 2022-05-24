from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.contactus import ContactUsView
from .views.aboutus import AboutUsView

from .auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('aboutus', AboutUsView.as_view(), name='aboutus'),
    path('contactus', ContactUsView.as_view(), name='contactus'),
    path('get/ajax/get_customer_address', CheckOut.as_view(), name="customer_addresses"),
]
