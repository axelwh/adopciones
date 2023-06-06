from django import forms
from apps_adopciones.mascota.models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'fecha_rescate',
            'edad_aproximada',
            'sexo',
            'persona',
            'vacuna',
            'imagen',
        ]

        labels = {
            'nombre': 'Nombre',
            'fecha_rescate': 'Fecha de rescate',
            'edad_aproximada': 'Edad aproximada',
            'sexo': 'Sexo',
            'persona': 'Adoptante',
            'vacuna': 'Vacuna',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }
