from xml.dom import ValidationErr

from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel
def car_filter_queryset(query:QueryDict)->QuerySet:
    qset = CarModel.objects.all()

    for k, v in query.items():
        match k:
            case 'price_gt':
                qset = qset.filter(price__gt=v)
            case 'price_lt':
                qset = qset.filter(price__lt=v)
            case 'price_gte':
                qset = qset.filter(price__gte=v)
            case 'price_lte':
                qset = qset.filter(price__lte=v)
            case 'find_model':
                qset = qset.filter(model=v)
            case 'find_start':
                qset = qset.filter(model__startswith=v)
            case 'find_end':
                qset = qset.filter(model__endswith=v)
            case 'ASC_model':
                qset = qset.all().order_by('model')
            case 'DESC_model':
                qset = qset.all().order_by('-model')
            case 'ASC_id':
                qset = qset.all().order_by('-id')
            case 'DESC_id':
                qset = qset.all().order_by('id')
            case 'ASCprice':
                qset = qset.all().order_by('-price')
            case 'DESC_iprice':
                qset = qset.all().order_by('price')
            case 'ASC_year':
                qset = qset.all().order_by('-year')
            case 'DESC_year':
                qset = qset.all().order_by('year')
            case _:
                raise ValidationError(f"{k} is not valid")
    return qset