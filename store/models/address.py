from django.db import models
from .customer import Customer
import datetime


class Address(models.Model):

    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    hno_and_street_or_lane = models.CharField(default=20, max_length=20)
    village_city_town = models.CharField(default=20,max_length=20)
    state = models.CharField(default=20, max_length=20)
    district = models.CharField(default=20, max_length=20)
    pin = models.IntegerField()
    country_code = models.CharField(default=20, max_length=20)
    phone = models.CharField(max_length=10, blank=True)
    default_address = models.BooleanField(default=False)
    insert_date = models.DateField(default=datetime.datetime.today)
    update_date = models.DateField(default=datetime.datetime.today)

    def save_address(self):
        self.save()

    @staticmethod
    def get_addresses_by_customer(customer_id):
        return Address.objects.filter(customer=customer_id).filter.order_by('-insert_date')

