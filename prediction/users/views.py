from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout as do_logout

# Create your views here.
class LoginView(TemplateView):
    template_name='login.html'
    def get(self, request, *args, **kwargs):
        context = {
            'titulo': 'Inicio de sesión',
            'form': AuthenticationForm()
        }
        try:
            if request.GET['error']:
                context['error'] = True
        except:
            if 'error' in context.keys():
                del(context['error'])
        return render(request, self.template_name, context)

class CheckView(TemplateView):
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # Hacemos el login manualmente
                login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
        return redirect('login/?error=True')

def logout(response):
    do_logout(response)
    return redirect('/login/')