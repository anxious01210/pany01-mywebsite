from django.db import models
from django.utils import timezone
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from tinymce import models as tinymce_models

# from django.db import models
# from django.conf import settings
# from django.shortcuts import reverse
# Create your models here.

class Brand(models.Model):
    """docstring for Brand."""

    name = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(null=False, unique=True, help_text="Do not enter any data here. This is an autopopulate fiels from 'Brand Name' field.")
    company_bio = models.TextField(blank=True, null=True)
    image_1 = models.ImageField(null=True, blank=True, upload_to="images/brands/", help_text='Brand image. WxH => 800x600')
    logo = models.ImageField(null=True, blank=True, upload_to="images/brands/", help_text='All Pages, Partner 1 Logo at "Our Experts". WxH => 113x49')
    logo_hover = models.ImageField(null=True, blank=True, upload_to="images/brands/", help_text='All Pages, Partner 1 Logo (hover in red) at "Our Experts". WxH => 113x49')

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('website:brand_detail', kwargs={'slug': self.slug})

    @property
    def image_1URL(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return url

    @property
    def logoURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url

    @property
    def logo_hoverURL(self):
        try:
            url = self.logo_hover.url
        except:
            url = ''
        return url


class CustomerTestimonial(models.Model):
    """docstring for CustomerTestimonial."""

    name = models.CharField(blank=True, max_length=100, help_text='Customer name.')
    slug = models.SlugField(null=False, unique=True, help_text='Do not enter any data here. This is an autopopulate fiels from "Customer Name" field.')
    testimonial = models.TextField(blank=True, max_length=2000)
    image_1 = models.ImageField(null=True, blank=True, upload_to="images/customers", help_text='Customer picture')

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

    @property
    def image_1URL(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return url


class Category(models.Model):
    """docstring for Category."""

    name = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(null=False, unique=True, help_text="Do not enter any data here. This is an autopopulate field from 'Category Name' field.")
    image_1 = models.ImageField(null=True, blank=True, upload_to="images/categories", help_text='Category picture. WxH => 370x300')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    @property
    def image_1URL(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return url

    # def get_absolute_url(self):
    #     return reverse('website:category_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    """docstring for Product."""

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands')
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, help_text='Product name.')
    slug = models.SlugField(null=False, unique=True, help_text='Do not enter any data here. This is an autopopulate field from "Product Name" field.')
    # description = tinymce_models.HTMLField(max_length=1000, blank=True, help_text='Description of the Product.')
    description = models.TextField(max_length=1000, blank=True, help_text='Description of the Product. you can use ( /br in <> ) between lines to make the the line appear in the next line.')
    image_1 = models.ImageField(null=True, blank=True, upload_to="images/products", help_text='1st image')
    image_2 = models.ImageField(null=True, blank=True, upload_to="images/products", help_text='2nd image')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    order = models.IntegerField(null=True, help_text='Ordering product view, from lowest to highest.')
    packaging = models.CharField(null=True, blank=True, max_length=10, default=' KG', help_text='Enter the package weight.')
    technical_manual = models.FileField(null=True, blank=True, upload_to="manuals/products")
    product_manual = models.FileField(null=True, blank=True, upload_to="manuals/products")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    features = models.CharField(blank=True, max_length=100)
    application = models.CharField(blank=True, max_length=100)
    # Added at 20221028 - Start
    type = models.CharField(blank=True, max_length=100)
    size = models.CharField(blank=True, max_length=100)
    mesh_size = models.CharField(blank=True, max_length=100)
    mass_per_unit = models.CharField(blank=True, max_length=100)
    weight = models.CharField(blank=True, max_length=100)
    shelf_life = models.CharField(blank=True, max_length=100)
    # roll_width = models.CharField(blank=True, max_length=100)
    # roll_length = models.CharField(blank=True, max_length=100)
    consumption = models.CharField(blank=True, max_length=100)
    coverage = models.CharField(blank=True, max_length=100)
    application_tools = models.CharField(blank=True, max_length=100)
    application_area = models.CharField(blank=True, max_length=100)
    mixing_ratio = models.CharField(blank=True, max_length=100)
    color = models.CharField(blank=True, max_length=100)
    thinner = models.CharField(blank=True, max_length=100)
    waiting_time_between_the_coats = models.CharField(blank=True, max_length=100)
    pot_life = models.CharField(blank=True, max_length=100)
    first_component = models.CharField(blank=True, max_length=100)
    second_component = models.CharField(blank=True, max_length=100)
    third_component = models.CharField(blank=True, max_length=100)
    composition = models.CharField(blank=True, max_length=100)
    tack_free_drying_time = models.CharField(blank=True, max_length=100)
    complete_drying_time = models.CharField(blank=True, max_length=100)
    density = models.CharField(blank=True, max_length=100)
    surface_temperature = models.CharField(blank=True, max_length=100)
    application_temprature = models.CharField(blank=True, max_length=100)
    dimensions = models.CharField(blank=True, max_length=100)
    length = models.CharField(blank=True, max_length=100)
    width = models.CharField(blank=True, max_length=100)
    surface = models.CharField(blank=True, max_length=100)
    thickness = models.CharField(blank=True, max_length=100)
    cutting_type = models.CharField(blank=True, max_length=100)
    body = models.CharField(blank=True, max_length=100)
    resistance = models.CharField(blank=True, max_length=100)
    resistance_to_solvents_and_oils = models.CharField(blank=True, max_length=100)
    resistance_to_acids_and_alkali = models.CharField(blank=True, max_length=100)
    thermal_conductivity = models.CharField(blank=True, max_length=100)
    fire_resistance = models.CharField(blank=True, max_length=100)
    compression_resistance = models.CharField(blank=True, max_length=100)
    compression_strength = models.CharField(blank=True, max_length=100)
    # Added at 20221028 - End


    class Meta:
        ordering = ('-order',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('website:product_detail', kwargs={'slug': self.slug})
        return reverse('website:product_detail', args=[self.id, self.slug])

    # def get_absolute_url(self):
    #     return reverse('website:product_detail', kwargs={'slug': self.id})
    #     # return reverse('website:product_detail', kwargs={'slug': self.slug})




    @property
    def image_1URL(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return url

    @property
    def image_2URL(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return url

    @property
    def technical_manualURL(self):
        try:
            url = self.technical_manual.url
        except:
            url = ''
        return url

    @property
    def product_manualURL(self):
        try:
            url = self.product_manual.url
        except:
            url = ''
        return url

class Project(models.Model):
    """docstring for Project."""

    CITY_CHOICES = (
        ('duhok', 'Duhok'),
        ('erbil', 'Erbil'),
        ('musil', 'Musil'),
        ('sulaimanya', 'Sulaimanya'),
        ('duhok', 'Duhok'),
        ('halabja', 'Halabja'),
        ('kerkuk', 'Kerkuk'),
        ('salahaddin', 'Salahaddin'),
        ('diyala', 'Diyala'),
        ('baghdad', 'Baghdad'),
        ('anbar', 'Anbar'),
        ('karbala', 'Karbala'),
        ('babil', 'Babil'),
        ('wasit', 'Wasit'),
        ('qadisyah', 'Qadisyah'),
        ('najaf', 'Najaf'),
        ('maysan', 'Maysan'),
        ('thiqar', 'Thiqar'),
        ('muthana', 'Muthana'),
        ('basra', 'Basra'),
    )


    name = models.CharField(blank=True, max_length=100, help_text='Project name')
    slug = models.SlugField(null=False, unique=True, help_text='Do not enter any data here. This is an autopopulate fiels from "Project Name" field.')
    city = models.CharField(blank=True, max_length=20, choices=CITY_CHOICES, help_text='Project city.')
    # city = models.CharField(blank=True, max_length=100, help_text='Project city.')
    challenge = models.TextField(blank=True, max_length=2000, help_text="What was the Client's Challenge.")
    categories = models.ManyToManyField(Category, max_length=100, help_text='The type of categories used in this project.')
    products = models.ManyToManyField(Product, max_length=100, help_text='The type of product(s) used in this project.')
    description_1 = models.TextField(blank=True, max_length=2000, help_text="Description for before the category was applied.")
    # description_2 = models.TextField(blank=True, max_length=2000, help_text="Description for after the category was applied.")
    image_1 = models.ImageField(null=True, blank=True, upload_to="images/projects", help_text='Project picture (the main picture), for project-list page. WxH => 370x300')
    # image_2 = models.ImageField(null=True, blank=True, upload_to="images/projects", help_text='Project picture, before category was applied. WxH => 770x530')
    # image_3 = models.ImageField(null=True, blank=True, upload_to="images/projects", help_text='Project picture, after the category was applied, for project-detail page. WxH => 770x530')
    order = models.IntegerField(null=True, help_text='Ordering project view, from lowest to highest.')

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('website:project_detail', kwargs={'slug': self.slug})


    @property
    def image_1URL(self):
        try:
            url = self.image_1.url
        except:
            url = ''
        return url

    @property
    def image_2URL(self):
        try:
            url = self.image_2.url
        except:
            url = ''
        return url
    @property
    def image_3URL(self):
        try:
            url = self.image_3.url
        except:
            url = ''
        return url

class Theme(models.Model):
    """docstring for Theme."""

    NAME_CHOICES = (
    ('theme_1', 'Theme_1'),
    ('theme_2', 'Theme_2'),
    ('theme_3', 'Theme_3'),
    ('theme_4', 'Theme_4'),
    ('theme_5', 'Theme_5'),
    ('theme_6', 'Theme_6'),
    ('theme_7', 'Theme_7'),
    ('theme_8', 'Theme_8'),
    ('theme_9', 'Theme_9'),
    ('theme_10', 'Theme_10'),
    )
    name = models.CharField(null=True, blank=True, max_length=10, choices=NAME_CHOICES, default='')
    default_theme = models.BooleanField(default=False)
    pany_logo = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text="All the Pages, PANY Co. Logo. WxH => WxH (doesn't matters as long as the size is less than 100KB)")
    pany_logo_retina = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='All the Pages, PANY Co. Logo_2x ... 4x or Retina (higher pixel density) screens Logo. WxH => 2-4x(pany_logo)')

    phone_number = models.CharField(blank=True, max_length=21, help_text='This is the Phone Number showed on each Topbar & Footer of the whole website. example ==> (+964) 750 450 6664')

    header_background_brand = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Brand_list & Brand_detail Pages, Header background image. WxH => 1920x366')
    header_background_category = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Category_list & Category_detail Pages, Header background image. WxH => 1920x366')
    header_background_project = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Project_list & Project_detail Pages, Header background image. WxH => 1920x366')
    header_background_product = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Product_list & Product_detail Pages, Header background image. WxH => 1920x366')
    header_background_about_us = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='About_us_list & About_us_detail Pages, Header background image. WxH => 1920x366')
    header_background_contact_us = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Contact_us_list & Contact_us_detail Pages, Header background image. WxH => 1920x366')
    header_background_document = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Document_list Pages, Header background image. WxH => 1920x366')

    slyder_image_1 = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Slyder 1 image. WxH => 1920x850')
    slyder_title_1 = models.CharField(null=True, blank=True, max_length=100, help_text='Home Page, Slyder 1 Title.')
    slyder_text_1 = models.CharField(null=True, blank=True, max_length=200, help_text='Home Page, Slyder 1 Text.')
    slyder_image_2 = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Slyder 2 image. WxH => 1920x850')
    slyder_title_2 = models.CharField(null=True, blank=True, max_length=100, help_text='Home Page, Slyder 2 Title.')
    slyder_text_2 = models.CharField(null=True, blank=True, max_length=200, help_text='Home Page, Slyder 2 Text.')
    slyder_image_3 = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Slyder 3 image. WxH => 1920x850')
    slyder_title_3 = models.CharField(null=True, blank=True, max_length=100, help_text='Home Page, Slyder 3 Title.')
    slyder_text_3 = models.CharField(null=True, blank=True, max_length=200, help_text='Home Page, Slyder 3 Text.')
    slyder_image_4 = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Slyder 4 image. WxH => 1920x850')
    slyder_title_4 = models.CharField(null=True, blank=True, max_length=100, help_text='Home Page, Slyder 4 Title.')
    slyder_text_4 = models.CharField(null=True, blank=True, max_length=200, help_text='Home Page, Slyder 4 Text.')
    slyder_image_5 = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Slyder 5 image. WxH => 1920x850')
    slyder_title_5 = models.CharField(null=True, blank=True, max_length=100, help_text='Home Page, Slyder 5 Title.')
    slyder_text_5 = models.CharField(null=True, blank=True, max_length=200, help_text='Home Page, Slyder 5 Text.')
    slyder_image_6 = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Slyder 6 image. WxH => 1920x850')
    slyder_title_6 = models.CharField(null=True, blank=True, max_length=100, help_text='Home Page, Slyder 6 Title.')
    slyder_text_6 = models.CharField(null=True, blank=True, max_length=200, help_text='Home Page, Slyder 6 Text.')
    slyder_image_7 = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Slyder 7 image. WxH => 1920x850')
    slyder_title_7 = models.CharField(null=True, blank=True, max_length=100, help_text='Home Page, Slyder 7 Title.')
    slyder_text_7 = models.CharField(null=True, blank=True, max_length=200, help_text='Home Page, Slyder 7 Text.')
    slyder_image_8 = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Slyder 8 image. WxH => 1920x850')
    slyder_title_8 = models.CharField(null=True, blank=True, max_length=100, help_text='Home Page, Slyder 8 Title.')
    slyder_text_8 = models.CharField(null=True, blank=True, max_length=200, help_text='Home Page, Slyder 8 Text.')

    quote_title = models.CharField(blank=True, max_length=100, help_text='Home Page, Title at "GET A QUOTE"')
    quote_text = models.CharField(blank=True, max_length=100, help_text='Home Page, Text at "GET A QUOTE"')

    intro_title = models.CharField(blank=True, max_length=100, help_text='Home Page, Title at "Count up introduction"')
    intro_description = models.TextField(blank=True, help_text='Home Page, Description at "Count up introduction"')
    sale_points = models.IntegerField(blank=True, null=True, help_text='Home Page, Number of Sale Points (Showroom) at "Count up introduction"')
    products = models.IntegerField(blank=True, null=True, help_text='Home Page, Number of Happy Products at "Count up introduction"')
    trucks_per_year = models.IntegerField(blank=True, null=True, help_text='Home Page, Number of Trucks/Year at "Count up introduction"')
    projects_supplied = models.IntegerField(blank=True, null=True, help_text='Home Page, Number of Projects Supplied at "Count up introduction"')
    experience_years = models.IntegerField(blank=True, null=True, help_text='Home Page, Number of Experience Years at "Count up introduction"')
    experience_years_image = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Page, Image at "Count up introduction". WxH => 270x360 is recommended.')

    about_us_text = models.TextField(blank=True, help_text='Home & about-us Pages, Text at "ABOUT USE"')
    about_us_signature = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home & about-us Pages, Signature at "ABOUT USE". WxH => 106x59 png transparent background.')
    about_us_name = models.CharField(blank=True, max_length=100, help_text='Home & about-us Pages, Name of the person at "ABOUT USE"')
    about_us_position = models.CharField(blank=True, max_length=100, help_text='Home & about-us Pages, Position of the person at "ABOUT USE"')
    about_us_image = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home & about-us Pages, Image at "ABOUT USE". WxH => YYYxYYY a sequare size is recommended.')

    our_category_text = models.TextField(blank=True, help_text='Home Page, Text at "OUR CATEGORY"')

    why_choose_use_1_title = models.CharField(blank=True, max_length=100, help_text='Home Page, Section 1 - Title at "Why Choose Us"')
    why_choose_use_1_text = models.CharField(blank=True, max_length=200, help_text='Home Page, Section 1 - Text at "Why Choose Us"')
    why_choose_use_2_title = models.CharField(blank=True, max_length=100, help_text='Home Page, Section 2 - Title at "Why Choose Us"')
    why_choose_use_2_text = models.CharField(blank=True, max_length=200, help_text='Home Page, Section 2 - Text at "Why Choose Us"')
    why_choose_use_3_title = models.CharField(blank=True, max_length=100, help_text='Home Page, Section 3 - Title at "Why Choose Us"')
    why_choose_use_3_text = models.CharField(blank=True, max_length=200, help_text='Home Page, Section 3 - Text at "Why Choose Us"')
    why_choose_use_image = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Pages, Image at "Why Choose Us". WxH => 570x370')

    background_categories = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Contact_us & home pages, form background Pages background image. WxH => 960x536')
    background_contact_us = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Contact_us & home pages, form background Pages background image. WxH => 960x600')

    footer_image = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='All Pages, Image for Footer background. WxH => 1920x366')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


    @property
    def header_background_brandURL(self):
        try:
            url = self.header_background_brand.url
        except:
            url = ''
        return url
    @property
    def header_background_categoryURL(self):
        try:
            url = self.header_background_category.url
        except:
            url = ''
        return url
    @property
    def header_background_projectURL(self):
        try:
            url = self.header_background_project.url
        except:
            url = ''
        return url
    @property
    def header_background_productURL(self):
        try:
            url = self.header_background_product.url
        except:
            url = ''
        return url
    @property
    def header_background_about_usURL(self):
        try:
            url = self.header_background_about_us.url
        except:
            url = ''
        return url
    @property
    def header_background_contact_usURL(self):
        try:
            url = self.header_background_contact_us.url
        except:
            url = ''
        return url
    @property
    def header_background_documentURL(self):
        try:
            url = self.header_background_document.url
        except:
            url = ''
        return url




    @property
    def slyder_image_1URL(self):
        try:
            url = self.slyder_image_1.url
        except:
            url = ''
        return url
    @property
    def slyder_image_2URL(self):
        try:
            url = self.slyder_image_2.url
        except:
            url = ''
        return url
    @property
    def slyder_image_3URL(self):
        try:
            url = self.slyder_image_3.url
        except:
            url = ''
        return url

    @property
    def slyder_image_4URL(self):
        try:
            url = self.slyder_image_4.url
        except:
            url = ''
        return url

    @property
    def slyder_image_5URL(self):
        try:
            url = self.slyder_image_5.url
        except:
            url = ''
        return url

    @property
    def slyder_image_6URL(self):
        try:
            url = self.slyder_image_6.url
        except:
            url = ''
        return url

    @property
    def slyder_image_7URL(self):
        try:
            url = self.slyder_image_7.url
        except:
            url = ''
        return url

    @property
    def slyder_image_8URL(self):
        try:
            url = self.slyder_image_8.url
        except:
            url = ''
        return url

    @property
    def pany_logoURL(self):
        try:
            url = self.pany_logo.url
        except:
            url = ''
        return url

    @property
    def pany_logo_retinaURL(self):
        try:
            url = self.pany_logo_retina.url
        except:
            url = ''
        return url

    @property
    def about_us_signatureURL(self):
        try:
            url = self.about_us_signature.url
        except:
            url = ''
        return url

    @property
    def about_us_imageURL(self):
        try:
            url = self.about_us_image.url
        except:
            url = ''
        return url

    @property
    def experience_years_imageURL(self):
        try:
            url = self.experience_years_image.url
        except:
            url = ''
        return url

    @property
    def why_choose_use_imageURL(self):
        try:
            url = self.why_choose_use_image.url
        except:
            url = ''
        return url

    @property
    def why_choose_use_imageURL(self):
        try:
            url = self.why_choose_use_image.url
        except:
            url = ''
        return url

    @property
    def background_categoriesURL(self):
        try:
            url = self.background_categories.url
        except:
            url = ''
        return url

    @property
    def background_contact_usURL(self):
        try:
            url = self.background_contact_us.url
        except:
            url = ''
        return url

    @property
    def footer_imageURL(self):
        try:
            url = self.footer_image.url
        except:
            url = ''
        return url

class Expert(models.Model):
    """docstring for Eperts."""

    name = models.CharField(blank=True, null=True, max_length=100, help_text='Home Pages, Expert number name at "Our Experts"')
    position = models.CharField(blank=True, null=True, max_length=100, help_text='Home Pages, Expert number position at PANY company at "Our Experts"')
    email = models.EmailField(blank=True, null=True, help_text='Home Pages, Expert number E-mail address at PANY company at "Our Experts"')
    phone_number = PhoneNumberField(blank=True, null=True, help_text='Home Pages, Expert number Phone number at PANY company at "Our Experts"')
    image = models.ImageField(null=True, blank=True, upload_to="images/themes/", help_text='Home Pages, Expert number Image at "Our Experts". WxH => 270x270 a sequare size is recommended.')

    class Meta:
        ordering = ('name',)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class SalePoint(models.Model):
    """docstring for SalePoint."""

    name = models.CharField(blank=True, null=True, max_length=100, help_text="Contact us Page, Sale Point's name")
    address = models.CharField(blank=True, null=True, max_length=100, help_text="Contact us Page, Sale Point's address")
    city = models.CharField(blank=True, null=True, max_length=100, help_text="Contact us Page, Sale Point's city")
    phone_number = PhoneNumberField(blank=True, null=True, help_text="Contact us Page, Sale Point's Phone Number")
    email = models.EmailField(help_text="Contact us Page, Sale Point's E-mail Address")
    active = models.BooleanField(default=True, help_text="Contact us Page, Only the active ones will be shown to the visitors")

    class Meta:
        ordering = ('city',)

    def __str__(self):
        return self.name
