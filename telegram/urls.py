from django.urls import path
from . import views


urlpatterns = [
    path('telegramuser/', views.TelegramUsersViewset.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),

    path('telegramuser/<int:pk>/', views.TelegramUsersViewset.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy'
        }
    )),
    path('user/', views.SubscriptionsViewset.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),

    path('user/<int:pk>/', views.SubscriptionsViewset.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy'
        }
    )),
    
    path('user_true/', views.TrueSubscriptionsViewset.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),

    path('user_true/<int:pk>/', views.TrueSubscriptionsViewset.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy'
        }
    )),
]
