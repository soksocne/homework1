from django.urls import path

from applications.account.views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view())
    ]