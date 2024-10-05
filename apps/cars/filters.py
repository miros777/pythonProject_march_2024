from django_filters import rest_framework as filters

from apps.cars.choices import BodyTypeChoice


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    range = filters.RangeFilter('year')  # range_min=1000 range_max=5000
    year_in = filters.BaseInFilter('year')
    body_type = filters.ChoiceFilter(field_name='body_type', choices=BodyTypeChoice.choices)
    model_end_with = filters.CharFilter(field_name='model', lookup_expr='endswith')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'model',
            'price'
        ))  # order=id  or order=-id

# CarModel.objects.filter(model__endswith=)
