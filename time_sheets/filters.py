import django_filters as dj_filters
from django.contrib.auth import get_user_model
from .models import TimeSheet
User = get_user_model()

class TimeSheetFilter(dj_filters.FilterSet):
    start_date = dj_filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = dj_filters.DateFilter(field_name="date", lookup_expr="lte")
    user = dj_filters.ModelChoiceFilter(field_name='user', queryset=User.objects.all())

    class Meta:
        model = TimeSheet
        fields = (
            'start_date',
            'end_date',
            'task',
            'user'
        )
