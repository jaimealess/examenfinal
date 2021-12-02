from django.db import models
from django.contrib import admin
#Define la clase Actor, esta tabla no se relaciona con nadie más.

class Alumno(models.Model):
    nombre_alumno  =   models.CharField(max_length=30)
    apellido_alumno  =   models.CharField(max_length=30)
    carne  =   models.CharField(max_length=30)
    genero  =   models.CharField(max_length=30)
    Municipio  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre_alumno

class Curso(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    alumnos   = models.ManyToManyField(Alumno, through='Cursado')

    def __str__(self):
        return self.nombre


class Cursado (models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


class CursadoInLine(admin.TabularInline):
    model = Cursado
#muestra una linea extra al momento de insertar, como indicación al usuario que se pueden ingresar varios actores.
    extra = 1


class AlumnoAdmin(admin.ModelAdmin):
    inlines = (CursadoInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (CursadoInLine,)