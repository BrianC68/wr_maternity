from django.urls import path
from . import views

app_name = 'making_marriage_work'

urlpatterns = [
    path('', views.MakingMarriageWorkClasses.as_view(), name='classes'),
    path('register/success/<pk>', views.MakingMarriageWorkClassBookingSuccess.as_view(), name='success'),
    path('register/<pk>/<slug:slug>/', views.CreateMakingMarriageWorkClassBooking.as_view(), name='register'),
    path('register/<pk>/', views.CreateMakingMarriageWorkClassBooking.as_view(), name='register'),
    path('register/', views.CreateMakingMarriageWorkClassBooking.as_view(), name='register'),
]
