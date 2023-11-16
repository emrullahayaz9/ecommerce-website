from django.forms import ModelForm
from .models import Order

class OrderModelForm(ModelForm):
    class Meta:
        model=Order
        fields = "__all__"
        
