from .models import Pdffile, AnnualCatalogue

def menu_pdffiles_types(request):
    types = list(Pdffile.objects.all().values_list('pdf_type', flat=True))

    final_list = []
    for c in types:
        if c not in final_list:
            final_list.append(c)

    return {'menu_pdffiles_types': final_list }

def menu_annual_catalogue(request):
    annual_catalogue = '#'
    try:
        annual_catalogue = list(AnnualCatalogue.objects.filter(status='published'))[0]
    except:
        pass

    # for c in annual_catalogue:
    #     annual_catalogue_url = c.catalogue_pdf_URL



    return {'menu_annual_catalogue': annual_catalogue }

