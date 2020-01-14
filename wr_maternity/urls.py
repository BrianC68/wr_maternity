from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from site_pages.views import HomePage, AboutPage, PaymentSuccess
from find_a_doula.views import DoulaListView

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('about/', AboutPage.as_view(), name='about'),
    path('admin/', admin.site.urls),
    path('childbirth_classes/', include('childbirth_classes.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact/', include('contact.urls')),
    path('doula_training/', include('doula_training.urls')),
    path('find_a_doula/', include('find_a_doula.urls')),
    path('find_a_midwife/', include('find_a_midwife.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/success/', PaymentSuccess.as_view(), name='payment-success'),
    path('resources/pregnancy-childbirth-services/doulas/', RedirectView.as_view(pattern_name='find_a_doula:doula-list', permanent=True)),
    path('resources/pregnancy-childbirth-services/childbirth-education/', RedirectView.as_view(pattern_name='childbirth_classes:classes', permanent=True)),
    path('find-a-midwife/', RedirectView.as_view(pattern_name='find_a_midwife:midwife-list', permanent=True)),
    path('doula-training-workshop/', RedirectView.as_view(pattern_name='doula_training:doula', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
