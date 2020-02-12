import django_filters
from .models import Product

class FoodFilter(django_filters.FilterSet):

    class Meta:
        model=Product
        fields=('name','description','amount','nicknames')