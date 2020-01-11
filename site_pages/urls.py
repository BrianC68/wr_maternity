
from django.urls import path
from . import views

# app_name = 'site_pages'

handler404 = 'wr_maternity.site_pages.views.handler404'

urlpatterns = [
    # path('', views.HomePage.as_view(), name='homepage'),
]