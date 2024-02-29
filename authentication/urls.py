from django.conf.urls import url

from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    url('users/register/', RegistrationAPIView.as_view(), name='register'),
    url('users/login/',LoginAPIView.as_view(), name='login'),
]