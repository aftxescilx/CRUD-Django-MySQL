from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Beneficiario
from .forms import BeneficiarioForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def beneficiarios(request):
    beneficiario = Beneficiario.objects.all()
    return render(request, 'beneficiario/index.html', {'beneficiario': beneficiario})

def crearBeneficiario(request):
    formulario = BeneficiarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('beneficiarios')
    return render(request, 'beneficiario/crear.html', {'formulario': formulario})

def editarBeneficiario(request, id):
    beneficiario = Beneficiario.objects.get(id=id)
    formulario = BeneficiarioForm(request.POST or None, request.FILES or None, instance=beneficiario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('beneficiarios')
    return render(request, 'beneficiario/editar.html', {'formulario': formulario})

def eliminarBeneficiario(request, id):
    beneficiario = Beneficiario.objects.get(id=id)
    beneficiario.delete()
    return redirect('beneficiarios')


