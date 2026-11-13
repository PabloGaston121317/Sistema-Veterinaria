from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AnimalForm, ClienteForm
import sqlite3
from .models import Cliente, Animal

def index(request, template_name= 'administracion/index.html'):
    return render(request, template_name, {
        'total_clientes': Cliente.objects.count(),
        'total_animales': Animal.objects.count()
    })


def lista_clientes(request, template_name= 'administracion/lista_clientes.html'):
    cliente_list = Cliente.objects.all()
    dato = {"clientes": cliente_list}
    return render(request,template_name, dato )

def lista_animales(resquest, template_name= 'administracion/lista_animales.html'):
    animal_list = Animal.objects.all()
    dato = {"animales": animal_list}
    return render(resquest, template_name, dato)

def cliente(request, num_dni, template_name= 'administracion/cliente.html'):
    cliente_objeto = Cliente.objects.get(dni = num_dni)     
    dato = {"cliente": cliente_objeto}
    return render(request, template_name, dato)


def animal(request, id, template_name= 'administracion/animal.html'):
    animal_objeto = Animal.objects.get(id = id)
    dato = {"animal": animal_objeto}
    return render(request, template_name, dato)

def nuevo_animal(request, template_name='administracion/nuevo_animal2.html'):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect("lista_animales")
    else:
        form = AnimalForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_cliente(request, template_name= 'administracion/nuevo_cliente.html'):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect("lista_clientes")
    else:
        form = ClienteForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def modificar_animal(request, pk, template_name= 'administracion/animal_form.html'):
    animal = Animal.objects.get(id = pk)
    form = AnimalForm(request.POST or None, instance=animal)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('lista_animales')
    dato = {"form": form}
    return render(request, template_name, dato)

def borrar_animal(request, pk, template_name='administracion/confirmacion_animal.html'):
    animal = Animal.objects.get(id = pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('lista_animales')
    dato = {"nombre": animal.nombre,
            "raza": animal.raza,
            "categoria": animal.categoria,
            "dueño": animal.duenio}
    return render(request, template_name, dato)

def modificar_cliente(request, pk, template_name = 'administracion/cliente_form.html'):
    cliente = Cliente.objects.get(id = pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('lista_clientes')
    dato = {"form": form}
    return render(request, template_name, dato)

def borrar_cliente(request, pk, template_name='administracion/confirmacion_cliente.html'):
    cliente = Cliente.objects.get(id = pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    dato = {"nombre": cliente.nombre,
            "apellido": cliente.apellido,
            "dni": cliente.dni}
    return render(request, template_name, dato)