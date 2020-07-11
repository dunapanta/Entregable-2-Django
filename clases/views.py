from django.http import HttpResponse
from django.shortcuts import render

from clases.models import Estudiante, Clase


def index(request):
    clases = Clase.objects.all()
    context = {
        'data': clases,
    }
    return render(request, 'clases/index.html', context)


def estudiantes(request):
    return HttpResponse('Aquí estan los estudiantes')

def estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)
    context = {
        'estudiante': estudiante
    }
    return render(request, 'clases/detail.html', context)
