from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Product

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'store/index.html'
    context_object_name = 'lastest_item'

    def get_queryset(self):
        return Product.objects.all()[:5]


class DetailView(generic.DetailView):
    template_name = 'store/detail.html'
    context_object_name = 'item'
    model = 'Product'

    def get_queryset(self):
        try:
            return Product.objects.filter(upccode=self.kwargs['pk'])
        except:
            raise Http404('hey, i tried.')
