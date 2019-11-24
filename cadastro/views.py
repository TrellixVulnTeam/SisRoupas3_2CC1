from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Funcionario, Cliente, Roupa
from .forms import *


def cadastrohome(request):
    context = {'mensagem' : 'Olá mundo2...'}
    return render(request, 'cadastro/index.html', context)

#-----------------Funcionarios------------------

def lista_funcionarios(request):
    funcionario = Funcionario.objects.all()
    form = FuncionarioForm()
    data = {'funcionario': funcionario, 'form': form}
    return render(request, 'cadastro/lista_funcionarios.html', data)


def funcionario_novo(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_funcionarios')

def funcionario_update(request, id):
    data = {}
    funcionario = Funcionario.objects.get(id=id)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    data['funcionario'] = funcionario
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadastro_lista_funcionarios')
    else:
        return render(request, 'cadastro/update_funcionario.html', data)

def funcionario_delete(request, id):
    funcionario = Funcionario.objects.get(id=id)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('cadastro_lista_funcionarios')
    else:
        return render(request, 'cadastro/delete_confirm.html', {'obj': funcionario})

#-------------Cliente----------------------


def cliente_novo(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_clientes')

def lista_clientes(request):
    cliente = Cliente.objects.all()
    form = ClienteForm()
    data = {'cliente' : cliente, 'form' : form}
    return render(request, 'cadastro/lista_clientes.html', data)

def cliente_update(request, id):
    data = {}
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    data['cliente'] = cliente
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadastro_lista_clientes')
    else:
        return render(request, 'cadastro/update_cliente.html', data)

def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cadastro_lista_clientes')
    else:
        return render(request, 'cadastro/delete_confirm.html', {'obj': cliente})


#----------Roupas --------------

def lista_roupas(request):
    roupa = Roupa.objects.all()
    form = RoupaForm()
    data = {'roupa' : roupa, 'form' : form}
    return render(request, 'cadastro/lista_roupas.html', data)

def roupa_novo(request):
    form = RoupaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_roupas')

def roupa_update(request, id):
    data = {}
    roupa = Roupa.objects.get(id=id)
    form = RoupaForm(request.POST or None, instance=roupa)
    data['roupa'] = roupa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadastro_lista_roupas')
    else:
        return render(request, 'cadastro/update_roupa.html', data)

def roupa_delete(request, id):
    roupa = Roupa.objects.get(id=id)
    if request.method == 'POST':
        roupa.delete()
        return redirect('cadastro_lista_roupas')
    else:
        return render(request, 'cadastro/delete_confirm.html', {'obj': roupa})
#------------MarcaRoupas---------

def lista_marcaroupas(request):
    marcaroupa = MarcaRoupa.objects.all()
    form = MarcaRoupaForm()
    data = {'marcaroupa' : marcaroupa, 'form' : form}
    return render(request, 'cadastro/lista_marcaroupas.html', data)

def marcaroupa_novo(request):
    form = MarcaRoupaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_marcaroupas')

def marcaroupa_update(request, id):
    data = {}
    marcaroupa = MarcaRoupa.objects.get(id=id)
    form = MarcaRoupaForm(request.POST or None, instance=marcaroupa)
    data['marcaroupa'] = marcaroupa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadastro_lista_marcaroupas')
    else:
        return render(request, 'cadastro/update_marcaroupa.html', data)

def marcaroupa_delete(request, id):
    marcaroupa = MarcaRoupa.objects.get(id=id)
    if request.method == 'POST':
        marcaroupa.delete()
        return redirect('cadastro_lista_marcaroupas')
    else:
        return render(request, 'cadastro/delete_confirm.html', {'obj': marcaroupa})

#-----------TipoRoupas----------

def lista_tiporoupas(request):
    tiporoupa = TipoRoupa.objects.all()
    form = TipoRoupaForm()
    data = {'tiporoupa' : tiporoupa, 'form' : form}
    return render(request, 'cadastro/lista_tiporoupas.html', data)

def tiporoupa_novo(request):
    form = TipoRoupaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_tiporoupas')

def tiporoupa_update(request, id):
    data = {}
    tiporoupa = TipoRoupa.objects.get(id=id)
    form = TipoRoupaForm(request.POST or None, instance=tiporoupa)
    data['tiporoupa'] = tiporoupa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadastro_lista_tiporoupas')
    else:
        return render(request, 'cadastro/update_tiporoupa.html', data)

def tiporoupa_delete(request, id):
    tiporoupa = TipoRoupa.objects.get(id=id)
    if request.method == 'POST':
        tiporoupa.delete()
        return redirect('cadastro_lista_tiporoupas')
    else:
        return render(request, 'cadastro/delete_confirm.html', {'obj': tiporoupa})

#--------Sessao--------------

def lista_sessao(request):
    sessao = Sessao.objects.all()
    form = SessaoForm()
    data = {'sessao' : sessao, 'form' : form}
    return render(request, 'cadastro/lista_sessao.html', data)

def sessao_novo(request):
    form = SessaoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('cadastro_lista_sessao')

def sessao_update(request, id):
    data = {}
    sessao = Sessao.objects.get(id=id)
    form = SessaoForm(request.POST or None, instance=sessao)
    data['sessao'] = sessao
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cadastro_lista_sessao')
    else:
        return render(request, 'cadastro/update_sessao.html', data)

def sessao_delete(request, id):
    sessao = Sessao.objects.get(id=id)
    if request.method == 'POST':
        sessao.delete()
        return redirect('cadastro_lista_sessao')
    else:
        return render(request, 'cadastro/delete_confirm.html', {'obj': sessao})
