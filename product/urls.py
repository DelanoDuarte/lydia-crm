from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('find', views.ProductSearchView.as_view(), name='search'),
    path('category/find', views.ProductSearchByCategoryView.as_view(), name='category_search'),
]   