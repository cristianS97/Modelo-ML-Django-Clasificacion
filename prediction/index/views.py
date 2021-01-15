from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import PredictionForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url='/login/'
    # Procesamos la respuesta de la vista
    def get(self, request, *args, **kwargs):
        context = {
            'titulo': 'My Clasification Site',
            'form': PredictionForm()
        }
        return render(request, self.template_name, context)