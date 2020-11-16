from django.shortcuts import render, redirect
from . import forms
from . import models


def emp(request):
    if request.method == 'POST':
        form = forms.EmpregadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('\show')
            except:
                pass
            else:
                form = forms.EmpregadoForm()
                return render(request, 'index.html', {'form': form})


def show(request):
    empregados = models.Empregado.objects.all()
    return render(request, 'show.html', {'empregados': empregados})


def edit(request, id):
    empregados = models.Empregado.objects.get(id=id)
    return render(request, 'edit.html', {'empregados': empregados})


def update(request, id):
    empregados = models.Empregado.objects.get(id=id)
    form = forms.EmpregadoForm(instance=empregados)
    if form.is_valid():
        form.save()
        return redirect('\show')
    return render(request, 'edit.html', {'empregados': empregados})


def delete(request, id):
    empregados = models.Empregado.objects.get(id=id)
    empregados.delete()
    return redirect('\show')

