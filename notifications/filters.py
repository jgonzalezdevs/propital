import django_filters
from notifications.models import Notification
from django.contrib.auth.models import User


class NotificationFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(choices=Notification.NOTIFICATION_TYPE_CHOICES)
    created_at__gte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')  
    is_read = django_filters.BooleanFilter()
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Notification
        fields = ['type', 'created_at__gte', 'created_at__lte', 'is_read']
