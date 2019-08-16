from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from .models import Usuario, Evento
from django.contrib.auth import authenticate


class RegistroUsuario(ModelForm):
    class Meta:
        model=Usuario
        fields='__all__'
        widgets = {
            'contrasena': TextInput(attrs={'size': 80, 'type': 'password'}),
            'nombres': TextInput(attrs={'size': 80}),
            'apellidos': TextInput(attrs={'size': 80}),
            #'identificacion': TextInput(attrs={'size': 80, 'type': 'number'}),
            'email': TextInput(attrs={'size': 80, 'type':'email'}),
            'identificacion': TextInput(attrs={'size': 80})
        }

    def clean(self):
        cleaned_data=super().clean()

class evento_form(ModelForm):
    class Meta:
        model=Evento
        fields='__all__'

    def clean(self):
        cleaned_data=super().clean()
