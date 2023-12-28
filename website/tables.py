# tutorial/tables.py
import django_tables2 as tables
from .models import SalePoint

class SalePointTable(tables.Table):
    class Meta:
        model = SalePoint
        # template_name = "django_tables2/bootstrap.html"
        template_name = "django_tables2/bootstrap4.html"
        # DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"
        fields = ("name", "address", "city", "phone_number", "email",)
