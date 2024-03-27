from django_filters import rest_framework as dj_filters
from .models import Lead


class LeadFilter(dj_filters.FilterSet):
    start_date = dj_filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = dj_filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Lead
        fields = (
            'start_date',
            'end_date',
            'status'
        )
