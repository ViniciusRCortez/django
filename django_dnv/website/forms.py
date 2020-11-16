from django import forms
from .models import Empregado


class EmpregadoForm(forms.ModelForm):
    class Meta:
        model = Empregado
        fields = '__all__'
