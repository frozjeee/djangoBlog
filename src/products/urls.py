from django.urls import path
from .views import (
    product_create_view,
    product_update_view,
    product_detail_view,
    delete_product_view,
    dynamic_lookup_view
)

app_name = 'products'
urlpatterns = [
    path('', product_detail_view, name="product-list"),
    path('create/', product_create_view, name="product-create"),
    path('<int:id>/', dynamic_lookup_view, name="product-detail"),
    path('<int:id>/update/', product_update_view, name="product-update"),
    path('<int:id>/delete/', delete_product_view, name="product-delete"),
]
