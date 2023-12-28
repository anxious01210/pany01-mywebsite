from django.shortcuts import render, get_object_or_404
from django.http import (Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
# from django.views import generic
# from django.views import generic
# from django.views.generic import DetailView
from django.urls import reverse
from django.views import generic
# from view_breadcrumbs import DetailBreadcrumbMixin
# from view_breadcrumbs import ListBreadcrumbMixin
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Product, Category, CustomerTestimonial, Project, Brand, Expert, SalePoint
from .filters import ProductFilter, SalePointFilter
from .tables import SalePointTable
from django.db.models import Q
import random


# Create your views here.

def home1(request):

    return render(request, 'website/home1.html')

def home(request):
    sent = False
    date = datetime.datetime.now()
    recent_projects = Project.objects.all()[0:6]
    testimonials = CustomerTestimonial.objects.all()
    # Before Edite, since the uploaded pics were too huge which Mr. Zaid Did it and it slowed dowsn the website.  ==>  products = Product.objects.all()
    products = list(Product.objects.all())
    products = random.sample(products, 30)
    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    brands = Brand.objects.all()
    # experts = Expert.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Send an email
            name = cd['name']
            message = cd['message']
            phone_number = cd['phone_number']
            city = cd['city']
            email = cd['email']
            # app.py
            #data_string = "The last season of BoJack Horseman was good"
            # initializing test list
            listA = ['crypto', 'Crytoemopeemope', 'Game of Thrones' , 'https://go.tygyguip.com/0j35']
            # printing original string
            #print("The original string : " + data_string)
            # printing original list
            #print("The original list : " + str(listA))
            # using list comprehension
            # checking if string contains list element
            if str(bool([ele for ele in listA if(ele in message)])):
                form = ContactForm()
                return render(request, 'website/home.html', {'date':date, 'brands': brands, 'form':form, 'sent': sent, 'recent_projects':recent_projects, 'products': products, 'testimonials': testimonials,})

            # print result
            # print("Does string contain any list element : " + str(bool(res)))

            # message = f" Name:_{name} \n Message:_ {message} \n City:_ {city} \n Phone Number:_ {phone_number} \n Customer E-mail:_ {email}"
            message = f" Dear {name}, \n \n Our team will get back to you with your request. \n \n Thanks and Regard. \n \n Name:_ {name} \n Message:_ {message} \n City:_ {city} \n Phone Number:_ {phone_number} \n Customer E-mail:_ {email} "
            # send_mail(cd['name'], message, 'rayan@panycompany.com', ['mehdi.a.majid@gmail.com', 'zaid@panycompany.com', 'info@panycompany.com'],)
            send_mail(cd['name'], message , 'info@panycompany.com', [f"{email}", 'zaid@panycompany.com',],)
            sent = True
            print('sent:', sent)

    else:
        form = ContactForm()

    return render(request, 'website/home.html', {'date':date, 'brands': brands, 'form':form, 'sent': sent, 'recent_projects':recent_projects, 'products': products, 'testimonials': testimonials,})




def BrandList(request):
    date = datetime.datetime.now()
    brands = Brand.objects.all()
    brand_count = brands.count()
    categories = Category.objects.all()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]

    paginator = Paginator(brands, 50) # 50 Brands in each page, although I need to add the pagination code to the page.
    page = request.GET.get('page')
    try:
        brands = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        brands = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        brands = paginator.page(paginator.num_pages)

    context = {'brands': brands, 'brand_count':brand_count, 'date':date, 'page': page, 'categories': categories}

    return render(request, 'website/brands/brand_list.html', context)

def BrandDetail(request, slug):
    date = datetime.datetime.now()
    brand = Brand.objects.get(slug=slug)
    brands = Brand.objects.all()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    return render(request, 'website/brands/brand_detail.html', {'brand': brand, 'brands': brands, 'date':date})


def CategoryList(request):
    date = datetime.datetime.now()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    categories = Category.objects.all()
    category_count = categories.count()
    brands = Brand.objects.all()

    if request.method == "POST":
        name = request.POST['p.name']
        show_categories = False
        # Added 2022-10-15 (Start)

        # products = Product.objects.filter(status='published')
        products = Product.objects.filter(Q(status='published') & Q(name__icontains=name))
        myFilter = ProductFilter(request.GET, queryset=products)
        products = myFilter.qs
        product_count = products.count()
        paginator = Paginator(myFilter.qs, 200) # 3 products in each page
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            products = paginator.page(paginator.num_pages)
        # Added 2022-10-15 (End)
        context = {'date': date, 'categories': categories, 'brands': brands, 'products': products, 'product_count': product_count, 'myFilter': myFilter, 'page': page, 'category_count': category_count, 'show_categories': show_categories}
        return render(request, 'website/categories/category_list.html', context)


    else:
        show_categories = False
        ct1 = []
        ct2 = []
        ct3 = []
        ct4 = []
        ct1 = categories[:7]
        ct2 = categories[7:14]
        ct3 = categories[14:21]
        ct4 = categories[21:28]

        # Added 2022-10-15 (Start)

        # products = Product.objects.filter(status='published')
        products = Product.objects.filter(status='published')
        myFilter = ProductFilter(request.GET, queryset=products)
        products = myFilter.qs
        product_count = products.count()
        paginator = Paginator(myFilter.qs, 40) # 3 products in each page
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            products = paginator.page(paginator.num_pages)
        # Added 2022-10-15 (End)
        context = {'date': date, 'categories': categories, 'brands': brands, 'products': products, 'product_count': product_count, 'myFilter': myFilter, 'page': page, 'category_count': category_count, 'ct1': ct1, 'ct2': ct2, 'ct3': ct3, 'ct4': ct4, 'show_categories': show_categories}
        return render(request, 'website/categories/category_list.html', context)

def ProductList(request, category_slug=None):
    date = datetime.datetime.now()
    category = None
    # categories = Category.objects.all()
    products = Product.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    product_count = products.count()
    # categories = Category.objects.all()
    brands = Brand.objects.all()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    paginator = Paginator(myFilter.qs, 40) # 3 products in each page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    context = {'category': category, 'products': products, 'product_count': product_count, 'myFilter': myFilter, 'brands': brands, 'page': page, 'date':date }
    return render(request, 'website/products/product_list.html', context)


# def ProductList(request):
#     date = datetime.datetime.now()
#     products = Product.objects.all().filter(status='published')
#     myFilter = ProductFilter(request.GET, queryset=products)
#     products = myFilter.qs
#     product_count = products.count()
#     brands = Brand.objects.all()
#     theme = Theme.objects.all().filter(default_theme=True)[:1]

#     paginator = Paginator(myFilter.qs, 12) # 3 products in each page
#     page = request.GET.get('page')
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         products = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         products = paginator.page(paginator.num_pages)

#     context = {'products': products, 'product_count': product_count, 'myFilter': myFilter, 'brands': brands, 'page': page, 'date':date}

#     return render(request, 'website/products/product_list.html', context)


# def ProductDetail(request, slug):
#     date = datetime.datetime.now()
#     product = Product.objects.get(slug=slug)
#     brands = Brand.objects.all()
#     theme = Theme.objects.all().filter(default_theme=True)[:1]
#     return render(request, 'website/products/product_detail.html', {'product': product, 'brands': brands, 'date':date})


def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, status='published')
    date = datetime.datetime.now()
    brands = Brand.objects.all()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]

    # readMore (start)
    splitat = 50
    description = product.description
    description01, description02 = description[:splitat], description[splitat:]
    # readMore (End)

    return render(request, 'website/products/product_detail.html', {'product': product, 'brands': brands, 'date':date, 'description': description, 'description01': description01, 'description02': description02})



def ProjectList(request):
    date = datetime.datetime.now()
    projects = Project.objects.all()
    project_count = projects.count()
    brands = Brand.objects.all()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    paginator = Paginator(projects, 100) # 3 posts in each page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)


    context = {'date': date, 'page': page, 'projects': projects, 'brands': brands, 'project_count': project_count}

    return render(request, 'website/projects/project_list.html', context)


def ProjectDetail(request, slug):
    date = datetime.datetime.now()
    project = Project.objects.get(slug=slug)
    brands = Brand.objects.all()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    return render(request, 'website/projects/project_detail.html', {'project': project, 'brands': brands, 'date':date})




def contact_us(request):
    sent = False
    date = datetime.datetime.now()
    brands = Brand.objects.all()
    testimonials = CustomerTestimonial.objects.all()

    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    sale_points = SalePoint.objects.all().filter(active=True)

    myFilter = SalePointFilter(request.GET, queryset=sale_points)
    sale_points = myFilter.qs
    sale_points_count = sale_points.count()

    paginator = Paginator(myFilter.qs, 50) # 3 products in each page
    page = request.GET.get('page')
    try:
        sale_points = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        sale_points = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        sale_points = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Send an email
            name = cd['name']
            message = cd['message']
            phone_number = cd['phone_number']
            city = cd['city']
            email = cd['email']
            listA = ['crypto', 'Crytoemopeemope', 'Game of Thrones' , 'https://go.tygyguip.com/0j35']
            # printing original string
            #print("The original string : " + data_string)
            # printing original list
            #print("The original list : " + str(listA))
            # using list comprehension
            # checking if string contains list element
            if str(bool([ele for ele in listA if(ele in message)])):
                form = ContactForm()
                context = {'date':date, 'brands': brands, 'form':form, 'sent': sent, 'sale_points': sale_points, 'sale_points_count': sale_points_count, 'page': page, 'myFilter': myFilter, 'testimonials': testimonials, }
                return render(request, 'website/contact-us.html', context)
            # auto_message = f"Dear {name}, \n \n Our team will will get back to you with with your request. \n \n Thanks and Regard."

            message = f" Dear {name}, \n \n Our team will get back to you with your request. \n \n Thanks and Regard. \n \n Name:_ {name} \n Message:_ {message} \n City:_ {city} \n Phone Number:_ {phone_number} \n Customer E-mail:_ {email} "

            send_mail(cd['name'], message , 'info@panycompany.com', [f"{email}", 'zaid@panycompany.com',],)
            sent = True
            print('sent:', sent)

    else:
        form = ContactForm()

    context = {'date':date, 'brands': brands, 'form':form, 'sent': sent, 'sale_points': sale_points, 'sale_points_count': sale_points_count, 'page': page, 'myFilter': myFilter, 'testimonials': testimonials, }
    return render(request, 'website/contact-us.html', context)

def AboutUs(request):
    date = datetime.datetime.now()
    brands = Brand.objects.all()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    return render(request, 'website/about-us.html', {'date':date, 'brands': brands})
