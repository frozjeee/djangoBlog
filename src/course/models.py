from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    # def get_absolute_url(self):
    #     return reverse("courses:courses-list", kwargs={"id": self.id})
