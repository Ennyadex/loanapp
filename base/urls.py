from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('customer/',views.customer),
    path('register/',views.register),
    path('login/',views.login)
]