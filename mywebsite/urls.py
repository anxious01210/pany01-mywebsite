"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import ProductSitemap, CategorySitemap

# for developement server or production - with the last line IF-Statement
from django.conf import settings

# from django.conf.urls.static import static
from filebrowser.sites import site

# django-filer CanonicalURL
from django.urls import re_path as url

sitemaps = {
    "products": ProductSitemap,
    "categories": CategorySitemap,
}

urlpatterns = [
    path("", include("website.urls", namespace="website")),
    path("library/", include("library.urls", namespace="library")),
    path("blog/", include("blog.urls", namespace="blog)")),
    path("tinymce/", include("tinymce.urls")),
    # path("admin/filebrowser/", include("site.urls")),
    url(r"^filer/", include("filer.urls")),
    path("admin/filebrowser/", site.urls),
    path("admin/", admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = (
        [
            path("__debug__/", include("debug_toolbar.urls")),
        ]
        + urlpatterns
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin.site.site_header = "PanyCompany Admin"
# admin.site.site_title = "PanyCompany Admin Portal"
# admin.site.index_title = "Welcome to PanyCompany Portal"

# #Modify Site Header
# admin.site.site_header = 'PanyCompany Admin'
# #Modify Site Title
# admin.site.site_title = "PanyCompany Admin Portal’"
# #Modify Site Index Title
# admin.site.index_title = "PanyCompany Portal"
# #Modify Site URL
# #admin.site.site_urls= "/admin"
