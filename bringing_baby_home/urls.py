from django.urls import path
from . import views

app_name = 'bringing_baby_home'

urlpatterns = [
    path('', views.BringingBabyHomeClassIndex.as_view(), name='classes'),
    path('register/success/<pk>', views.BringingBabyHomeClassBookingSuccess.as_view(), name='success'),
    path('register/<pk>/<slug:slug>/', views.CreateBringingBabyHomeClassBooking.as_view(), name='register'),
    path('register/<pk>/', views.CreateBringingBabyHomeClassBooking.as_view(), name='register'),
    path('register/', views.CreateBringingBabyHomeClassBooking.as_view(), name='register'),
]