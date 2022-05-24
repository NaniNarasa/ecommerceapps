from django.db import models


class ContactUs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    subscribe = models.CharField(max_length=3)

    # to save the data
    def register(self):
        self.save()
        return ""
