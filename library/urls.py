from django.urls import path
from . import views
# from django.urls import reverse
# from django_filters.views import FilterView
# from .models import *
# from .filters import ProductFilter


app_name = 'library'

urlpatterns = [
    path('', views.DocList, name='pdffile_list'),
]