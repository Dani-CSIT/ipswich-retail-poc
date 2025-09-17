from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from shop.views import product_detail, product_list


def health(_):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", product_list, name="home"),
    path("p/<str:sku>/", product_detail, name="product-detail"),
    path("healthz/", health, name="healthz"),
]
