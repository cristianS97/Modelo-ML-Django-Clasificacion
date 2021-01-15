from django import forms

class PredictionForm(forms.Form):
    Ri = forms.FloatField(min_value=0, label='Ri', required=True)
    Na = forms.FloatField(min_value=0, label='Na', required=True)
    Mg = forms.FloatField(min_value=0, label='Mg', required=True)
    Al = forms.FloatField(min_value=0, label='Al', required=True)
    Si = forms.FloatField(min_value=0, label='Si', required=True)
    K = forms.FloatField(min_value=0, label='K', required=True)
    Ca = forms.FloatField(min_value=0, label='Ca', required=True)
    Ba = forms.FloatField(min_value=0, label='Ba', required=True)
    Fe = forms.FloatField(min_value=0, label='Fe', required=True)