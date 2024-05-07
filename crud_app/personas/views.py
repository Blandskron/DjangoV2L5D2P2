# personas/views.py
from django.shortcuts import render, redirect
from .models import Persona

def crear_persona(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        ciudad = request.POST['ciudad']
        Persona.objects.create(nombre=nombre, edad=edad, ciudad=ciudad)
        return redirect('listar_personas')
    return render(request, 'personas/crear_persona.html')

def listar_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/listar_personas.html', {'personas': personas})

def filtrar_personas(request):
    if request.method == 'POST':
        ciudad = request.POST['ciudad']
        personas = Persona.objects.filter(ciudad=ciudad)
        return render(request, 'personas/listar_personas.html', {'personas': personas})
    return render(request, 'personas/filtrar_personas.html')

def excluir_personas(request):
    if request.method == 'POST':
        ciudad = request.POST['ciudad']
        personas = Persona.objects.exclude(ciudad=ciudad)
        return render(request, 'personas/listar_personas.html', {'personas': personas})
    return render(request, 'personas/excluir_personas.html')

def ordenar_personas(request):
    personas = Persona.objects.all().order_by('nombre')
    return render(request, 'personas/listar_personas.html', {'personas': personas})


def actualizar_persona(request, id):
    persona = Persona.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        ciudad = request.POST['ciudad']
        persona.nombre = nombre
        persona.edad = edad
        persona.ciudad = ciudad
        persona.save()
        return redirect('listar_personas')
    return render(request, 'personas/actualizar_persona.html', {'persona': persona})

def eliminar_persona(request):
    if request.method == 'POST':
        id_persona = request.POST['id']
        Persona.objects.get(id=id_persona).delete()
        return redirect('listar_personas')
    return render(request, 'personas/eliminar_persona.html')
