from django.shortcuts import render
from .models import Pdffile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
# from website.models import Theme
# Create your views here.

def DocList(request):
    date = datetime.datetime.now()
    # theme = Theme.objects.all().filter(default_theme=True)[:1]
    pdffiles = Pdffile.objects.filter(status='published')
    pdffiles_count = pdffiles.count()

    paginator = Paginator(pdffiles, 100) # 100 posts in each page
    page = request.GET.get('page')
    try:
        pdffiles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        pdffiles = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        pdffiles = paginator.page(paginator.num_pages)


    context = {'date': date, 'page': page,  'pdffiles': pdffiles, 'pdffiles_count': pdffiles_count, }
    return render(request, 'library/pdffile/library_list.html', context)