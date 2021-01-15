from django.shortcuts import render
from django.views.generic.base import TemplateView
import joblib
from .models import InputData, Clasification
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ResultView(LoginRequiredMixin, TemplateView):
    login_url='/login'
    template_name='result.html'
    def post(self, request, *args, **kwargs):
        rcls = joblib.load('finalized_model.sav')

        data = list()
        
        data.append(request.POST['Ri'])
        data.append(request.POST['Na'])
        data.append(request.POST['Mg'])
        data.append(request.POST['Al'])
        data.append(request.POST['Si'])
        data.append(request.POST['K'])
        data.append(request.POST['Ca'])
        data.append(request.POST['Ba'])
        data.append(request.POST['Fe'])

        rcls = joblib.load('finalized_model.sav')
        answer = rcls.predict([data])

        prediction_data = Clasification.objects.get(pk=answer)

        data_input = InputData.objects.create(ri=request.POST['Ri'],
                                    na=request.POST['Na'],
                                    mg=request.POST['Mg'],
                                    al=request.POST['Al'],
                                    si=request.POST['Si'],
                                    k=request.POST['K'],
                                    ca=request.POST['Ca'],
                                    ba=request.POST['Ba'],
                                    fe=request.POST['Fe'],
                                    prediction=prediction_data)

        context = {
            'titulo': 'Result of the clasification',
            'data': data,
            'pred': prediction_data
        }

        return render(request, self.template_name, context)
