from django import forms
from .models import Curso, Alumno


class CursoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Curso
        fields = ('nombre', 'anio', 'alumnos')

    def __init__ (self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields["alumnos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumnos"].help_text = "Ingrese los Alumnos asignados al curso"
        self.fields["alumnos"].queryset = Alumno.objects.all()
