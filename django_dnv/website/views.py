from django.shortcuts import render, redirect
from django_dnv.website.forms import EmpregadoForm
from django_dnv.website.models import Empregado


def emp(request):
    if request.method == 'POST':
        form = EmpregadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('\show')
            except:
                pass
            else:
                form = EmpregadoForm()
                return render(request, 'index.html', {'form': form})


def show(request):
    empregados = Empregado.objects.all()
    return render(request, 'show.html', {'empregados': empregados})


def edit(request, id):
    empregados = Empregado.objects.get(id=id)
    return render(request, 'edit.html', {'empregados': empregados})


def update(request, id):
    empregados = Empregado.objects.get(id=id)
    form = EmpregadoForm(instance=empregados)
    if form.is_valid():
        form.save()
        return redirect('\show')
    return render(request, 'edit.html', {'empregados': empregados})


def delete(request, id):
    empregados = Empregado.objects.get(id=id)
    empregados.delete()
    return redirect('\show')

