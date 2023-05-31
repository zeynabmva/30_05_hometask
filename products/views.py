from django.shortcuts import render
from .models import Product
from django.db.models import F, FloatField
from django.db.models.functions import Coalesce
# Create your views here.
def product_list_view(request):
    products = Product.objects.annotate(
        discount=Coalesce("discount_price" , 0 ,output_field = FloatField()),
        total_price=F("price") - F("discount")
    )
    context = {
        "products":products
    }
    return render(request , "products/list.html" , context)


def product_detail_view(request ,id):
    product = Product.objects.annotate(
        discount=Coalesce("discount_price" , 0 ,output_field = FloatField()),
        total_price=F("price") - F("discount")
    ).get(id=id)

    context = {
        "product" :product
    }
    return render(request , "products/detail.html" , context)