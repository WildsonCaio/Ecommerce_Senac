from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'    

class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.IntegerField()
    like = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)      
    product = models.ManyToManyField(Products)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Cart'       
