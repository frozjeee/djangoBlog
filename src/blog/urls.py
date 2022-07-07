from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name="article-list"),
    path('<int:id>/', ArticleDetailView.as_view(), name="article-detail"),
    path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="article-update"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="article-delete"),
    # path('create/', product_create_view, name="product-create"),
    # path('<int:id>/', dynamic_lookup_view, name="product-detail"),
    # path('<int:id>/update/', prod uct_update_view, name="product-update"),
    # path('<int:id>/delete/', delete_product_view, name="product-delete"),
]
