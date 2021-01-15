from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from pred.models import InputData

# Create your views here.
class DataView(LoginRequiredMixin, ListView):
    template_name = 'datos.html'
    paginate_by = 10
    model = InputData
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Data on BBDD'
        context['total'] = len(InputData.objects.all().order_by('-created'))
        return context





