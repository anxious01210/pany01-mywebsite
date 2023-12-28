from .models import Category, Brand, Project, Theme

def menu_categories(request):
    categories = Category.objects.all()

    return {'menu_categories': categories}

def menu_brands(request):
    brands = Brand.objects.all()

    return {'menu_brands': brands}

def menu_projects_cities(request):
    cities = list(Project.objects.all().values_list('city', flat=True))

    final_list = []
    for c in cities:
        if c not in final_list:
            final_list.append(c)



    return {'menu_projects_cities': final_list }


# theme = Theme.objects.all().filter(default_theme=True)[:1]

def theme(request):
    # annual_catalogue = '#'
    try:
        # annual_catalogue = list(AnnualCatalogue.objects.filter(status='published'))[0]
        # theme = list(Theme.objects.all().filter(default_theme=True)[:1])[0]
        theme = Theme.objects.all().filter(default_theme=True)[:1] # (from 0 to 1) or [0:1] ==> makes it iterable **!!**
    except:
        pass

    # for c in annual_catalogue:
    #     annual_catalogue_url = c.catalogue_pdf_URL



    return {'theme': theme }