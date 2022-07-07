from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    summary = models.TextField()
    available = models.BooleanField(default=True)

    def get_absolute_url_view(self):
        return reverse("products:product-detail", kwargs={"id": self.id})

    def get_absolute_url_delete(self):
        return reverse("products:product-delete", kwargs={"id": self.id})

    def get_absolute_url_update(self):
        return reverse("products:product-update", kwargs={"id": self.id})
