from django import forms
from django_dnv.website.models import Empregado


class EmpregadoForm(forms.ModelForm):
    class Meta:
        model = Empregado
        fields = '__all__'
