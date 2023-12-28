from django.urls import path
from . import views
from django.urls import reverse
from django_filters.views import FilterView
from .models import *
from .filters import ProductFilter


app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.CategoryList, name='category_list'),
    path('brands/', views.BrandList, name='brand_list'),
    path('brands/<slug:slug>/', views.BrandDetail, name='brand_detail'),
    path('products/', views.ProductList, name='product_list'),
    path('products/<slug:category_slug>/', views.ProductList, name='product_list_by_category'),
    path('products/<int:id>/<slug:slug>/', views.ProductDetail, name='product_detail'),
    path('projects/', views.ProjectList, name='project_list'),
    path('projects/<slug:slug>/', views.ProjectDetail, name='project_detail'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.AboutUs, name='about_us'),
]


