from django.contrib.auth import get_user_model
from django.db.models import Q
import django_filters as dj_filters
from .models import Lead

User = get_user_model()

class LeadFilter(dj_filters.FilterSet):
    start_date = dj_filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = dj_filters.DateFilter(field_name="date", lookup_expr="lte")
    user = dj_filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Lead
        fields = (
            'start_date',
            'end_date',
            'status',
            'user'
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and not user.is_superuser:
            self.filters['user'] = dj_filters.ModelChoiceFilter(queryset=User.objects.filter(id=user.id))

    @property
    def qs(self):
        parent = super().qs
        if self.request and not self.request.user.is_superuser:
            return parent.filter(Q(user=self.request.user) | Q(manager=self.request.user))
        return parent
