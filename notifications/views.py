from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer
from notifications.filters import NotificationFilter
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters   
from rest_framework.response import Response
from rest_framework import status


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filterset_class = NotificationFilter

    def destroy(self, request, *args, **kwargs):
        """
        Elimina todas las notificaciones del usuario autenticado.
        """
        Notification.objects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        """
        Filtrar notificaciones por usuario
        """
        user = self.request.user.id
        return self.queryset.filter(user=user)
    
    def dispatch(self, request, *args, **kwargs):
        print(self.request.body)
        return super().dispatch(request, *args, **kwargs)