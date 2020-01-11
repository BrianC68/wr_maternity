from django.urls import path
from .views import MidwifeListView, MidwifeDetailView

app_name = 'find_a_midwife'

urlpatterns = [
    path('', MidwifeListView.as_view(), name='midwife-list'),
    path('<slug:slug>/', MidwifeDetailView.as_view(), name='midwife-detail'),
    
]