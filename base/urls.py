from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.home, name="dashboard"),
    path('customer/',views.customer),
    path('allcustomers/',views.allcustomers, name="allcustomers"),
    path('register/',views.register),
    path('',views.login, name="login"),
    path('appadmin/',views.appadmin),
    path('status/',views.status, name="status"),
    path('edit_status/<str:pk>/', views.editstatus, name="edit_status"),
]