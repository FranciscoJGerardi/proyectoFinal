from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *
class AutosFormularios(forms.Form):
    nombreUsuario= forms.CharField(max_length=50)
    marca= forms.CharField(max_length=20)
    modelo= forms.CharField(max_length=20)
    año= forms.IntegerField()
    kilometros= forms.IntegerField()
    descripcion= forms.CharField(max_length=250)
    precio= forms.IntegerField()

class AsesoramientoFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    telefono= forms.IntegerField()
    dataDeAsesoramiento= forms.CharField(max_length=250)
    modeloDelAuto= forms.CharField(max_length=50)

class EditarUsuario(UserChangeForm):

    password= forms.CharField(help_text="", widget= forms.HiddenInput(), required=False)
    password1= forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        password2= self.cleaned_data["password2"]

        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no son iguales")
        return password2
    
class AvatarFormulario(forms.ModelForm):
   class Meta:
      model=Avatar
      fields=('imagen',)  