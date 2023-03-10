from django.db import models
from django.contrib.auth.models import User


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
    commentable = models.BooleanField(default=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)