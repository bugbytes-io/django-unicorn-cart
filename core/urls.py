from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path(
        'accounts/login/',
        LoginView.as_view(template_name='core/login.html'),
        name='login'
    ),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('', views.cart, name='cart'),
]
