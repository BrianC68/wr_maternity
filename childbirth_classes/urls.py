from django.urls import path
from . import views

app_name = 'childbirth_classes'

urlpatterns = [
    path('', views.ChildbirthClassIndex.as_view(), name='classes'),
    path('register/success/<pk>', views.ChildbirthClassBookingSuccess.as_view(), name='success'),
    path('register/<pk>/<slug:slug>/', views.CreateChildbirthClassBooking.as_view(), name='register'),
    path('register/<pk>/', views.CreateChildbirthClassBooking.as_view(), name='register'),
    path('register/', views.CreateChildbirthClassBooking.as_view(), name='register'),
]