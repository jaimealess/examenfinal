from django.contrib import admin
from .models import Alumno, AlumnoAdmin, Curso, CursoAdmin

# Register your models here.

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Curso, CursoAdmin)