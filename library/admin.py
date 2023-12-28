from django.contrib import admin
from .models import AnnualCatalogue, Pdffile
from django import forms
from django.contrib import messages

# Register your models here.

@admin.register(AnnualCatalogue)
class AnnualCatalogueAdmin(admin.ModelAdmin):
    list_display = ('filename', 'catalogue_pdf', 'order_number', 'status')
    search_fields = ['filename', 'catalogue_pdf']
    list_filter = ('status', )
    def save_model(self, request, obj, form, change):
        try:
            stored_catalogue_pdf = AnnualCatalogue.objects.get(pk=obj.pk).catalogue_pdf
            print('stored_catalogue_pdf:  ==>  ', stored_catalogue_pdf)
            if change:
                if stored_catalogue_pdf != obj.catalogue_pdf:
                    print('==>  stored_catalogue_pdf is changed!')
                    stored_catalogue_pdf.delete(save=False)
        except:
            pass

        return super().save_model(request, obj, form, change)

@admin.register(Pdffile)
class PdffileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'pdf', 'coverpage', 'pagenumforcover', 'pdf_type', 'status')
    list_filter = ('pdf_type', 'status')
    search_fields = ['question_text']
    readonly_fields = ('coverpage', )
    def save_model(self, request, obj, form, change):
        update_fields = []
        if change:
            if form.initial['pagenumforcover'] != form.cleaned_data['pagenumforcover']:
                update_fields.append('pagenumforcover')
            if form.initial['filename'] != form.cleaned_data['filename']:
                update_fields.append('filename')
            try:
                stored_pdf = Pdffile.objects.get(pk=obj.pk).pdf
                print('stored_pdf:  ==>  ', stored_pdf)

                if stored_pdf != obj.pdf:
                    print('==>  stored_pdf is changed!')
                    stored_pdf.delete(save=False)


            except:
                pass

        obj.save(update_fields=update_fields)
        super().save_model(request, obj, form, change)

