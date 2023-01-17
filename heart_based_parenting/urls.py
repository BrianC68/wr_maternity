from django.urls import path
from . import views

app_name = 'heart_based_parenting'

urlpatterns = [
    path('', views.HeartBasedParentingClassIndex.as_view(), name='classes'),
    
]