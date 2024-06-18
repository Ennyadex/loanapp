from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.home, name="dashboard"),
    path('customer/',views.customer),
    path('editcustomers/',views.editcustomers, name="editcustomers"),
    path('user_signup/',views.user_signup),
    path('',views.login_user, name="login"),
    path('appadmin/',views.appadmin),
    path('status/',views.status, name="status"),
    path('viewstatus/',views.viewstatus, name="viewstatus"),
    path('editstatus/<str:pk>/<str:customer>/', views.editstatus, name="editstatus"),
    path('updatestatus/', views.updatestatus, name="updatestatus"),
    path('deletecustomer/<str:pk>', views.deletecustomer, name="deletecustomer"),
    path('customerinfo/',views.customerinfo, name="customerinfo"),
    path('editall/<str:pk>/<str:name>/<str:address>/<str:phone_number>/<str:gender>/<str:state>/<str:loan_offer>', views.editall, name="editall"),
    path('updateall/', views.updateall, name="updateall"),
    path('interest/', views.interest, name="interest"),
    path('applyloan/', views.applyloan, name="applyloan"),
    path('logout/', views.loggedout, name="logout"),
    
]