from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save, pre_save
from pdf2image import convert_from_path
from django.conf import settings
import os


# Create your models here.

COVER_PAGE_DIRECTORY = 'library/coverdirectory/'
PDF_DIRECTORY = 'library/pdfdirectory/'
COVER_PAGE_FORMAT = 'jpg'


# this function is used to rename the pdf to the name specified by filename field
def set_pdf_file_name(instance, filename):
    return os.path.join(PDF_DIRECTORY, '{}.pdf'.format(instance.filename))

# not used in this example
def set_cover_file_name(instance, filename):
    return os.path.join(COVER_PAGE_DIRECTORY, '{}.{}'.format(instance.filename, COVER_PAGE_FORMAT))

class Pdffile(models.Model):
    # validator checks file is pdf when form submitted
    pdf = models.FileField(
        upload_to=set_pdf_file_name,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        help_text = "After uploading a pdf from here and saving it, do not change the pdf. If you you need to then delete this object completely and create a new one with the new pdf file."
        )
    filename = models.CharField(max_length=100, help_text = "This is the name that will show to the website visitors. Make it to be less than 25 characters.")
    TYPE_CHOICES = (
        ('manual', 'Manual'),
        ('catalogue', 'Catalogue'),
        ('application_details', 'Application Details'),
    )
    pdf_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', help_text = "'Draft' will cause the pdf to not to be loaded/shown to the website visitors.")
    pagenumforcover = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)], help_text = "Choose the page number that you want the system to create a cover image from it to be shown to the website visitors.")
    coverpage = models.FileField(blank=True, upload_to=set_cover_file_name)

    @property
    def coverpage_URL(self):
        try:
            url = self.coverpage.url
        except:
            url = ''
        return url
    def __str__(self):
        return self.filename

    @property
    def pdfURL(self):
        try:
            url = self.pdf.url
        except:
            url = ''
        return url

def convert_pdf_to_image(sender, instance, created, update_fields, **kwargs):
    if created:  # or 'pagenumforcover' in update_fields
        # check if COVER_PAGE_DIRECTORY exists, create it if it doesn't
        # have to do this because of setting coverpage attribute of instance programmatically
        cover_page_dir = os.path.join(settings.MEDIA_ROOT, COVER_PAGE_DIRECTORY)

        if not os.path.exists(cover_page_dir):
            os.mkdir(cover_page_dir)

        # convert page cover (in this case) to jpg and save
        cover_page_image = convert_from_path(
            pdf_path=instance.pdf.path,
            dpi=50,
            first_page=instance.pagenumforcover,
            last_page=instance.pagenumforcover,
            fmt=COVER_PAGE_FORMAT,
            output_folder=cover_page_dir,
            )[0]

        # get name of pdf_file
        pdf_filename, extension = os.path.splitext(os.path.basename(instance.pdf.name))
        new_cover_page_path = '{}.{}'.format(os.path.join(cover_page_dir, pdf_filename), COVER_PAGE_FORMAT)
        # rename the file that was saved to be the same as the pdf file
        os.rename(cover_page_image.filename, new_cover_page_path)
        # get the relative path to the cover page to store in model
        new_cover_page_path_relative = '{}.{}'.format(os.path.join(COVER_PAGE_DIRECTORY, pdf_filename), COVER_PAGE_FORMAT)
        instance.coverpage = new_cover_page_path_relative

        # call save on the model instance to update database record
        instance.save()
    elif update_fields:
        cover_page_dir = os.path.join(settings.MEDIA_ROOT, COVER_PAGE_DIRECTORY)

        if not os.path.exists(cover_page_dir):
            os.mkdir(cover_page_dir)

        # convert page cover (in this case) to jpg and save
        cover_page_image = convert_from_path(
            pdf_path=instance.pdf.path,
            dpi=50,
            first_page=instance.pagenumforcover,
            last_page=instance.pagenumforcover,
            fmt=COVER_PAGE_FORMAT,
            output_folder=cover_page_dir,
            )[0]

        # get name of pdf_file
        pdf_filename, extension = os.path.splitext(os.path.basename(instance.pdf.name))
        new_cover_page_path = '{}.{}'.format(os.path.join(cover_page_dir, pdf_filename), COVER_PAGE_FORMAT)
        # rename the file that was saved to be the same as the pdf file
        os.rename(cover_page_image.filename, new_cover_page_path)
        # get the relative path to the cover page to store in model
        new_cover_page_path_relative = '{}.{}'.format(os.path.join(COVER_PAGE_DIRECTORY, pdf_filename), COVER_PAGE_FORMAT)
        instance.coverpage = new_cover_page_path_relative

        # call save on the model instance to update database record
        instance.save()

post_save.connect(convert_pdf_to_image, sender=Pdffile)



# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=Pdffile)
def Pdffile_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.coverpage.delete(False)
    instance.pdf.delete(False)


class AnnualCatalogue(models.Model):
    filename = models.CharField(max_length=100, help_text='Enter the file-name here.')
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', help_text = "'Published' will cause the pdf to to be loaded/shown to the website visitors.")
    catalogue_pdf = models.FileField(
        upload_to='library/YearCatalogueDirectory/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
        )
    order_number = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)], help_text = "The PDF with the status 'Published' & lowest order number (1 2 3 ...) will be displayed as Annual Catalogue to the visitors.")
    class Meta:
        ordering = ['order_number']
    @property
    def catalogue_pdf_URL(self):
        try:
            url = self.catalogue_pdf.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.filename

@receiver(pre_delete, sender=AnnualCatalogue)
def AnnualCatalogue_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.catalogue_pdf.delete(False)