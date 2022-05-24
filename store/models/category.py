from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        print("inside get_all_categories() of Category class")
        return Category.objects.all()

    def __str__(self):
        return self.name
