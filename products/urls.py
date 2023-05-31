from django.urls import path
from . import views



urlpatterns = [
    path("list/" , views.product_list_view , name="product-list"),
    path("create/" , views.created_view , name="product-create"),
    path("list/detail/<id>/" , views.product_detail_view , name="product-detail")

]