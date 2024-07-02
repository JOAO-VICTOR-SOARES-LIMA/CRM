from django.shortcuts import render, redirect
from .models import Oportunity


'''from django.form import OportunityForm'''



# Create your views here.


'''def criar_oportunidade(request):
    if request.method == 'POST':
        form = OportunidadeForm(request.POST)
        if form.is_valid():
            form.save()'''

'''def list_oportunity(request):
    opportunities = TB_OPORTUNITY.objects.all()
    return render(request, 'opportunities.html', {'oportunities': opportunities})
    

def create_oportunity(request):
    if request.method == 'POST':
        form = OportunityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opportunities.html')
        else:
            print('Erro 404')'''

def delete():
    Oportunity.objects.all().delete()

def home(request):
    '''lista = {
        'Samuel',
        'Joao',
        'Daniel',
        'Douglas',
        'Marcio',
        'Fabio',
    }'''
    lista = Oportunity.objects.all()
    context = {
        'lista': lista,
    }
    
    return render(request, 'opportunities.html', context)

def listagem(request):
    '''oportunidades = Oportunity.objects.all()
    return (request, 'listagem.html')'''
    context = {
        'name': 'Joao',
        'idade': '21' ,  
    }
    return (request, 'listagem.html', context)


def salvar(request):
    name = request.POST.get("name")
    Oportunity.objects.create(name=name)
    lista = Oportunity.objects.all()
    context = {
        'lista': lista,
    }
    return render(request, "opportunities.html", context)
'''def salvar(request):
    if request.method == 'POST':
        vname = request.POST.get("name")
        Oportunity.objects.create(name=vname)
    lista = Oportunity.objects.all()
    return render(request, "opportunities.html", {'lista':lista})'''
        


    
            