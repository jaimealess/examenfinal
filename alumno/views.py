from django.shortcuts import render
from django.contrib import messages
from .forms import CursoForm
from .models import Cursado,Curso

def alumno_nuevo(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for alumno_id in request.POST.getlist('alumnos'):
                cursado = Cursado(alumno_id=alumno_id, curso_id = curso.id)
                cursado.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardado Exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'alumnos/alumno_editar.html', {'formulario': formulario})