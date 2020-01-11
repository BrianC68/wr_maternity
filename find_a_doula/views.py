from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Doula


class DoulaListView(ListView):
    '''Page that displays all doulas.'''

    template_name = 'doula_list_view.html'
    model = Doula
    context_object_name = 'doulas'

    def get_queryset(self):
        queryset = super().get_queryset().only('name', 'service_area', 'photo')
        return queryset


class DoulaDetailView(DetailView):
    '''Page that displays individual doula details.'''

    template_name = 'doula_detail_view.html'
    model = Doula
    context_object_name = 'doula'
