import django_filters
from django_filters import DateFilter, CharFilter
from .models import SalePoint, Product


class SalePointFilter(django_filters.FilterSet):
    """docstring for SalePointFilter."""
    # name = django_filters.CharFilter(lookup_expr='iexact')
    # start_date = DateFilter(field_name='publish_date', lookup_expr='gte')
    # end_date = DateFilter(field_name='publish_date', lookup_expr='lte')
    # description = CharFilter(field_name='description', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = SalePoint
        # exclude = ['image_1', 'image_2', 'technical_manual', 'product_manual', ]
        # fields = '__all__'
        fields = ['name', 'city']

        # class CategoryFilter(django_filters.FilterSet):
        #     """docstring for CategoryFilter."""
        #     # name = django_filters.CharFilter(lookup_expr='iexact')
        #     # start_date = DateFilter(field_name='publish_date', lookup_expr='gte')
        #     # end_date = DateFilter(field_name='publish_date', lookup_expr='lte')
        #     description = CharFilter(field_name='description', lookup_expr='icontains')
        #
        #     class Meta:
        #         model = Category
        #         # exclude = ['image_1', 'image_2', 'technical_manual', 'product_manual', ]
        #         # fields = '__all__'
        #         fields = ['name','description']



class ProductFilter(django_filters.FilterSet):
    """docstring for ProductFilter."""
    # name = django_filters.CharFilter(lookup_expr='iexact')
    # start_date = DateFilter(field_name='publish_date', lookup_expr='gte')
    # end_date = DateFilter(field_name='publish_date', lookup_expr='lte')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'brand', 'category', 'description' ]
        # fields = {'name': ['icontains'],}
        # exclude = ['image_1', 'image_2', 'technical_manual', 'product_manual', 'description', 'category', 'brand']
        # fields = '__all__'
        # fields = ['name', 'brand', 'category', 'description']
        # fields = ['name', 'brand', 'category', 'description']
        # filter_overrides = {
        #      models.CharField: {
        #          'filter_class': django_filters.CharFilter,
        #          'extra': lambda f: {
        #              'lookup_expr': 'icontains',
        #          },
        #      },
        #      models.BooleanField: {
        #          'filter_class': django_filters.BooleanFilter,
        #          'extra': lambda f: {
        #              'widget': forms.CheckboxInput,
        #          },
        #      },
        #  }
# import django_filters
# from django_filters import DateFilter, CharFilter
#
# from .models import *
#
# class Ps4Filter(django_filters.FilterSet):
#     """docstring for Ps4Filter."""
#
#     # start_date = DateFilter(field_name='publish_date', lookup_expr='gte')
#     # end_date = DateFilter(field_name='publish_date', lookup_expr='lte')
#     description = CharFilter(field_name='description', lookup_expr='icontains')
#
#     class Meta:
#         model = Ps4
#         fields = '__all__'
#         exclude = ['games', 'image', 'price_paypal', 'region_code', 'publish_date', 'sold', 'price_btc', 'region_country',]
