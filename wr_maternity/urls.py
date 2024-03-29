from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView
from django.contrib import admin
from site_pages.views import HomePage, AboutPage, PaymentSuccess
from find_a_doula.views import DoulaListView

# added to remove sidebar and fix admin
admin.autodiscover()
admin.site.enable_nav_sidebar = False

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
    path('heart-based-parenting/', include('heart_based_parenting.urls')),
    path('bringing-baby-home/', include('bringing_baby_home.urls')),
    path('making-marriage-work/', include('making_marriage_work.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/success/', PaymentSuccess.as_view(), name='payment-success'),
    # path('report_builder/', include('report_builder.urls')),
    path('resources/pregnancy-childbirth-services/doulas/', RedirectView.as_view(pattern_name='find_a_doula:doula-list', permanent=True)),
    path('resources/pregnancy-childbirth-services/childbirth-education/', RedirectView.as_view(pattern_name='childbirth_classes:classes', permanent=True)),
    path('find-a-midwife/', RedirectView.as_view(pattern_name='find_a_midwife:midwife-list', permanent=True)),
    path('doula-training-workshop/', RedirectView.as_view(pattern_name='doula_training:doula', permanent=True)),
    path('google8e677ef3f646420f.html', (TemplateView.as_view(
        template_name = 'google8e677ef3f646420f.html',
        content_type = 'text/html')),
        name='google8e677ef3f646420f.html'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
