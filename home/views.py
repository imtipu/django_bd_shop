from django.shortcuts import render

# Create your views here.
from django.views.generic import *

from shop.models import Product


class HomeIndex(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeIndex, self).get_context_data(**kwargs)
        context['title'] = 'Homepage'
        context['products'] = Product.objects.all()[:10]
        return context
