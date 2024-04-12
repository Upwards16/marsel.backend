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
    @property
    def qs(self):
        parent = super().qs
        user = self.request.user

        if user.position and user.position.name == 'admin':
            return parent

        elif user.position and user.position.name == 'Менеджер по продажам':
            return parent.filter(user=user)

        else:
            return parent.none()
