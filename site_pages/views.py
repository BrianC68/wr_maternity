from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render
from . import models


class HomePage(TemplateView):
    template_name = 'index.html'
    model = models.Page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.model.objects.all().filter(title='Home')
        context['title'] = page[0].title
        context['description'] = page[0].description
        context['keywords'] = page[0].keywords
        context['content'] = page[0].content
        return context


class AboutPage(TemplateView):
    template_name = 'about.html'


@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccess(TemplateView):
    template_name = 'payment_success.html'


def handler404(request, exception, template_name='404.html'):
    response = render('404.html')
    reson.status_code = 404
    return response
