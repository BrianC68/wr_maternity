
from django.urls import path
from . import views

app_name = 'doula_training'

urlpatterns = [
    path('', views.DoulaTrainingIndex.as_view(), name='doula'),
    path('register/success/<pk>', views.DoulaWorkshopBookingSuccess.as_view(), name='success'),
    path('register/<pk>/<location>/<slug:slug>/', views.CreateDoulaWorkshopBooking.as_view(), name='register'),
    path('register/<pk>/<location>/', views.CreateDoulaWorkshopBooking.as_view(), name='register'),
    path('register/', views.CreateDoulaWorkshopBooking.as_view(), name='register'),
    ]
