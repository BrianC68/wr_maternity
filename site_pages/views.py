from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


class HomePage(TemplateView):
    template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccess(TemplateView):
    template_name = 'payment_success.html'


def handler404(request, exception, template_name='404.html'):
    response = render('404.html')
    reson.status_code = 404
    return response
