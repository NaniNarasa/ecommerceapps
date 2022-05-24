from django.db import models
from .product import Products
from .customer import Customer
from .address import Address
import datetime


class Order(models.Model):

    order_id = models.IntegerField(default=1000)
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.CharField(default="Initiate", max_length=30)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id, status):
        return Order.objects.filter(customer=customer_id).filter(status=status).order_by('-date')

    @staticmethod
    def get_max_order_id():
        return Order.objects.get('order_id').order_by("-order_id")

