from django.urls import path
from . import views



urlpatterns = [
    path("list/" , views.product_list_view),
    path("list/detail/<id>/" , views.product_detail_view)
]