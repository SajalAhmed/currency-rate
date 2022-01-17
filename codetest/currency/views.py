from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.db.models import Q
from codetest.currency.models import Convert, Currency 

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['converts'] = Convert.objects.all()
        return context


class DataTable(ListView):
    model = Currency
    template_name = "ajax.html"
    context_object_name = "currency"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('search', '')
        if search:
            return Currency.objects.filter(Q(name__icontains=search)).distinct() #__icontains for case sensitive search
        return super().get_queryset(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        limit = self.request.GET.get('limit')
        _sl = 1
        _lm = 10
        if page:
            _sl = int(page)
        if limit:
            _lm = int(limit)
        context['sl_count'] = (_sl * _lm - (_lm - 1)) - 1

        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('limit', self.paginate_by)

    def get_ordering(self):
        ordering = self.request.GET.get('order_by', 'id')
        return ordering
