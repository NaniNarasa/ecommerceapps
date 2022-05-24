from django.db import models
from store.models import Products


class ProductInventory(models.Model):
    product_id = models.ForeignKey(Products, blank=True, null=True, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    max_count_to_cart = models.IntegerField()

    @staticmethod
    def get_inventory_count(product_id):
        print("inside get_inventory_count() of ProductInventory class")
        return ProductInventory.objects.get(product_id=product_id)

