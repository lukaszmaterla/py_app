from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('<int:id>/update/', product_update_view, name='product-update'),
    # path('<int:id>/delete/', product_delete_view, name='product-delete'),
]