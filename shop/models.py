from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300) # because images usually stored in the different servers and can accesiable with url
    
    def __str__(self):
        return f"{self.title}  {self.price} {self.description}"
class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

class Order(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    address = models.TextField()
    products = models.ForeignKey(Cart, on_delete=models.CASCADE)