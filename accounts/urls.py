from django.urls import path
from . import views

urlpatterns = [
    path("c/login", views.customer_login, name="clogin"),
    path("s/login", views.seller_login, name="slogin"),
    path("c/register", views.customer_register, name="cregister"),
    path("s/register", views.seller_register, name="sregister"),
    path('logout', views.logout_view, name='logout')
]