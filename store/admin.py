from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.contactus import ContactUs
from .models.product_inventory import ProductInventory


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ContactUs)
admin.site.register(ProductInventory)

# username = narasareddy, email = narasareddy@yahoo.com, password = Nani@1226
