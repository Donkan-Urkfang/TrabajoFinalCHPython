from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Entregable.models import Avatar, Profile



class FormJuego(forms.Form):
    nombre = forms.CharField()
    genero = forms.CharField()
    fechaDeLanzamiento = forms.DateField()
    plataforma = forms.IntegerField()
    imagen = forms.ImageField()
     
class FormDesarrolladora(forms.Form):
    nombre = forms.CharField()
    pais = forms.CharField()
    ciudad = forms.IntegerField()
    contacto = forms.IntegerField()
    imagen = forms.ImageField()


### USER SETTINGS ###


class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Surname")
    email = forms.EmailField(label="Modify Email")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password1', 'password2' ]

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('user', 'imagen',)


### REGISTER ###

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Valid password only.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already register")
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']