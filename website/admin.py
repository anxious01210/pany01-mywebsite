from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product, Brand, Category, CustomerTestimonial, Project, Theme, Expert, SalePoint

# Register your models here.



@admin.register(Theme)
class ThemeAdmin(ImportExportModelAdmin):
    list_display = ('name', 'default_theme', 'slyder_title_1',)
    list_filter = ('default_theme', )
    search_fields = ('name', 'slyder_title_1', 'slyder_text_1', 'slyder_title_2', 'slyder_text_2', 'slyder_title_3', 'slyder_text_3', 'quote_title', 'quote_text', 'about_us_text',)
    # prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', )

@admin.register(Expert)
class ExpertAdmin(ImportExportModelAdmin):  # class ExpertAdmin(admin.ModelAdmin): ==> class ExpertAdmin(ImportExportModelAdmin):
    list_display = ('name', 'position', 'email', 'phone_number')
    list_filter = ('name', )
    search_fields = ('name', 'position', 'email', 'phone_number')
    ordering = ('name', )

@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    list_display = ('name', 'company_bio', 'logo',)
    list_filter = ('name', )
    search_fields = ('name', 'name', 'company_bio')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', )

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('brand', 'id', 'name', 'category', 'status', 'order',)
    list_filter = ('brand', 'category', 'status')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'status', 'order')

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'id')
    list_filter = ('name',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(CustomerTestimonial)
class CustomerTestimonialAdmin(ImportExportModelAdmin):
    list_display = ('name', 'testimonial',)
    list_filter = ('name',)
    search_fields = ('name', 'testimonial')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('name', 'city', 'challenge')
    list_filter = ('name', 'city',)
    search_fields = ('name', 'city', 'description_1', 'challenge')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(SalePoint)
class SalePointAdmin(ImportExportModelAdmin):
    list_display = ('name', 'address', 'city', 'phone_number', 'email', 'active')
    list_filter = ('city', 'active')
    search_fields = ('name', 'address', 'city', 'phone_number', 'email')
    ordering = ('name',)
