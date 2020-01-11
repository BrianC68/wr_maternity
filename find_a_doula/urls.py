from django.urls import path
from .views import DoulaListView, DoulaDetailView

app_name = 'find_a_doula'

urlpatterns = [
    path('', DoulaListView.as_view(), name='doula-list'),
    path('<slug:slug>/', DoulaDetailView.as_view(), name='doula-detail'),
    
]