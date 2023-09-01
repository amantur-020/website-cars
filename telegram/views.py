import django_filters
from rest_framework import filters,viewsets
from .models import TelegramUsers,Subscriptions
from .serializers import TelegramUsersSerializers,SubscriptionsSerializers


class TelegramUsersViewset(viewsets.ModelViewSet):
    queryset=TelegramUsers.objects.all()
    serializer_class=TelegramUsersSerializers
    filter_backends=(django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields=("user_id",)



class SubscriptionsViewset(viewsets.ModelViewSet):
    queryset=Subscriptions.objects.all()
    serializer_class=SubscriptionsSerializers
    filter_backends=(django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields=("user__user_id",)



class TrueSubscriptionsViewset(viewsets.ModelViewSet):
    queryset=Subscriptions.objects.filter(is_active=True)
    serializer_class=SubscriptionsSerializers
    filter_backends=(django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields=("user__user_id",)