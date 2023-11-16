from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('detail/<int:id>', views.detail,name="detail"),
    path('cart/<int:id>', views.cart,name="cart"),
    path('just_cart', views.just_cart,name="just_cart"),
    path('delete', views.delete,name="delete"),
    path('checkout', views.checkout, name="checkout")
]
