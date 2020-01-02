from django.urls import path, include
from .views import UserView, UserCreateView, UserListCreateView

app_name = 'accounts'


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', UserView.as_view(), name='test'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('list-create/', UserListCreateView.as_view(), name='list-create'),
]
