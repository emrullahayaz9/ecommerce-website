from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Products, Cart, Order
from django.core.paginator import Paginator
from .forms import OrderModelForm
def index(request):
    product_objects = Products.objects.all()

    item_name = request.GET.get('item_name')
    # search code
    if item_name!='' and item_name is not None:
        product_objects = Products.objects.filter(title__icontains=item_name)
    # paginator code
    paginator = Paginator(product_objects,4) # 2. argüman 1 sayfadakaç ürünün olması, kaç item'dan sonra paginate edecegini söylüyor
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {"product_objects":product_objects})

def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, "shop/detail.html", {"product_object":product_object})
def cart(request, id):
    product = Products.objects.get(id=id)
    cart_object = Cart(product=product)
    cart_object.save()
    product_objects =Products.objects.all()
    return render(request, 'shop/index.html', {"product_objects":product_objects})


def delete(request):
    Cart.objects.all().delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/")
def just_cart(request):
    cart = Cart.objects.all()
    return render(request, "shop/cart.html", {"cart":cart})
def checkout(request):
    form = OrderModelForm()
    if request.method=="GET":
        return render(request, "shop/checkout.html", {"form":form})
    if request.method=="POST":
        form = OrderModelForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/")