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
from .models import Product, Solution, CustomerTestimonial, Project, Brand, Theme, Expert, SalePoint
from .filters import ProductFilter, SolutionFilter, SalePointFilter
from .tables import SalePointTable

# Create your views here.

def home1(request):

    return render(request, 'website/home1.html')

def home(request):
    sent = False
    date = datetime.datetime.now()
    solutions = Solution.objects.all().filter(status='published')[0:6]
    recent_projects = Project.objects.all()[0:6]
    testimonials = CustomerTestimonial.objects.all()
    products = Product.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]
    brands = Brand.objects.all()
    experts = Expert.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Send an email

            send_mail(cd['name'], cd['message'], 'rayan@panycompany.com', ['mehdi.a.majid@gmail.com'],)
            sent = True
            print('sent:', sent)

    else:
        form = ContactForm()

    return render(request, 'website/home.html', {'date':date, 'theme':theme, 'brands': brands, 'experts':experts, 'form':form, 'sent': sent, 'solutions': solutions, 'recent_projects':recent_projects, 'products': products, 'testimonials': testimonials,})

def BrandList(request):
    date = datetime.datetime.now()
    brands = Brand.objects.all()
    brand_count = brands.count()
    theme = Theme.objects.all().filter(default_theme=True)[:1]

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

    context = {'brands': brands, 'brand_count':brand_count, 'date':date, 'page': page, 'theme':theme}

    return render(request, 'website/brands/brand_list.html', context)

def BrandDetail(request, slug):
    date = datetime.datetime.now()
    brand = Brand.objects.get(slug=slug)
    brands = Brand.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]
    return render(request, 'website/brands/brand_detail.html', {'brand': brand, 'brands': brands, 'date':date, 'theme':theme})

def ProductList(request):
    date = datetime.datetime.now()
    products = Product.objects.all().filter(status='published')
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    product_count = products.count()
    brands = Brand.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]

    paginator = Paginator(myFilter.qs, 12) # 3 products in each page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)

    context = {'products': products, 'product_count': product_count, 'myFilter': myFilter, 'brands': brands, 'page': page, 'date':date, 'theme':theme}

    return render(request, 'website/products/product_list.html', context)




def ProductDetail(request, slug):
    date = datetime.datetime.now()
    product = Product.objects.get(slug=slug)
    brands = Brand.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]
    return render(request, 'website/products/product_detail.html', {'product': product, 'brands': brands, 'date':date, 'theme':theme})


def SolutionList(request):

    sent = False
    date = datetime.datetime.now()
    solutions = Solution.objects.all().filter(status='published')
    myFilter = SolutionFilter(request.GET, queryset=solutions)
    solutions = myFilter.qs
    solution_count = solutions.count()
    brands = Brand.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]

    paginator = Paginator(myFilter.qs, 20) # 3 posts in each page
    page = request.GET.get('page')
    try:
        solutions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        solutions = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        solutions = paginator.page(paginator.num_pages)

    testimonials = CustomerTestimonial.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Send an email

            send_mail(cd['name'], cd['message'], 'rayan@panycompany.com', ['mehdi.a.majid@gmail.com'],)
            sent = True
            print('sent:', sent)


    else:

        form = ContactForm()
        # solutions = Solution.objects.all().filter(status='published')

    context = {'solutions': solutions, 'solution_count': solution_count, 'myFilter': myFilter, 'brands': brands, 'page': page, 'date':date, 'form':form, 'sent': sent, 'testimonials': testimonials, 'theme':theme}
    return render(request, 'website/solutions/solution_list.html', context)



def SolutionDetail(request, slug):
    date = datetime.datetime.now()
    solution = Solution.objects.get(slug=slug)
    related_products = solution.product_set.all()
    brands = Brand.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]
    # print('related products:_ ', related_products )
    return render(request, 'website/solutions/solution_detail.html', {'solution': solution, 'brands': brands, 'date':date, 'theme':theme })


def ProjectList(request):
    date = datetime.datetime.now()
    projects = Project.objects.all()
    project_count = projects.count()
    brands = Brand.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]
    paginator = Paginator(projects, 6) # 3 posts in each page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)

    solutions = Solution.objects.all().filter(status='published')

    context = {'date': date, 'page': page, 'projects': projects, 'brands': brands, 'project_count': project_count, 'solutions': solutions, 'theme':theme}

    return render(request, 'website/projects/project_list.html', context)


def ProjectDetail(request, slug):
    date = datetime.datetime.now()
    project = Project.objects.get(slug=slug)
    brands = Brand.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]
    r_solutions = project.solutions.filter(status='published')
    return render(request, 'website/projects/project_detail.html', {'project': project, 'brands': brands, 'r_solutions': r_solutions, 'date':date, 'theme':theme})




def contact_us(request):
    sent = False
    date = datetime.datetime.now()
    brands = Brand.objects.all()

    theme = Theme.objects.all().filter(default_theme=True)[:1]
    table = SalePointTable(SalePoint.objects.all().filter(active=True))
    table.paginate(page=request.GET.get("page", 1), per_page=30)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Send an email

            send_mail(cd['name'], cd['message'], 'rayan@panycompany.com', ['mehdi.a.majid@gmail.com'],)
            sent = True
            print('sent:', sent)

    else:
        form = ContactForm()
    return render(request, 'website/contact-us.html', {'date':date, 'brands': brands, 'form':form, 'theme':theme, 'sent': sent, 'table': table })

def AboutUs(request):
    date = datetime.datetime.now()
    brands = Brand.objects.all()
    theme = Theme.objects.all().filter(default_theme=True)[:1]
    solutions = Solution.objects.all().filter(status='published')[:6]
    return render(request, 'website/about-us.html', {'date':date, 'brands': brands, 'theme':theme, 'solutions': solutions})
