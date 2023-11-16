from django.contrib import admin
from .models import Products, Cart, Order
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Order)