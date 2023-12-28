from django.contrib.sitemaps import Sitemap
from .models import Product, Category

class ProductSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Product.objects.all().filter(status='published')

    def lastmod(self, obj):
        return obj.updated

class CategorySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.4

    def items(self):
        return Category.objects.all().filter(status='published')

    def lastmod(self, obj):
        return obj.updated
