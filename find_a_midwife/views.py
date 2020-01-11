from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Midwife


class MidwifeListView(ListView):
    '''Page that displays all midwives.'''

    template_name = 'midwife_list_view.html'
    model = Midwife
    context_object_name = 'midwives'

    def get_queryset(self):
        queryset = super().get_queryset().only('name', 'service_area', 'photo')
        return queryset


class MidwifeDetailView(DetailView):
    '''Page that displays individual doula details.'''

    template_name = 'midwife_detail_view.html'
    model = Midwife
    context_object_name = 'midwife'
