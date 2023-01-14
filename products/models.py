from django.db import models


class Phone(models.Model):
    image = models.ImageField(blank=True, null=True)
    brand = models.CharField(max_length=255)
    phone_model = models.CharField(max_length=100)
    descriptions = models.TextField()
    memory = models.CharField(max_length=30)
    color = models.CharField(max_length=50)
    price = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    rate = models.FloatField()