from django import db
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from Entregable.models import Avatar, Juego, Desarrolladora
from Entregable.forms import AvatarForm, FormDesarrolladora, FormJuego, UserRegisterForm, ProfileUpdateForm, UserUpdateForm, UserEditForm
from django.contrib import messages

from django.db import connection


def  register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Entregable/Registro.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Entregable/Profile.html', context)
    


def inicio(request):
    return render(request, "Entregable/Inicio.html", )

def about(request):
    return render(request, "Entregable/About.html")

def contact(request):
    return render(request, "Entregable/Contact.html")

def paginas(request):
    tables = connection.introspection.table_names()
    return render(request, "Entregable/Paginas.html",{ "tables": tables})



def juegos(request):
    lista_juegos = Juego.objects.all()
    return render(request, "Entregable/Juegos.html", {"lista": lista_juegos})

class JuegoList(LoginRequiredMixin ,ListView):
    model= Juego
    template_name= "Entregable/JuegoList.html"

class JuegoDetail(DetailView):
    model= Juego
    template_name= "Entregable/JuegoDetail.html"

class JuegoUpdate(UpdateView):
    model= Juego
    success_url= "/Entregable/listaJuego"
    fields= ["nombre", "genero", "fechaDeLanzamiento", 'plataforma', "imagen"]
    template_name= "Entregable/JuegoUpdate.html"

class JuegoDelete(DeleteView):
    model= Juego
    success_url= "/Entregable/listaJuego"
    template_name= "Entregable/JuegoConfirmDelete.html"

class JuegoCreate(CreateView):
    model= Juego
    success_url= "/Entregable/listaJuego"
    fields= ["nombre", "genero", "fechaDeLanzamiento",'plataforma', "imagen"]
    template_name= "Entregable/JuegoNew.html"





class DesarrolladoraList(LoginRequiredMixin ,ListView):
    model= Desarrolladora
    template_name= "Entregable/DesarrolladoraList.html"

class DesarrolladoraDetail(DetailView):
    model= Desarrolladora
    template_name= "Entregable/DesarrolladoraDetail.html"

class DesarrolladoraUpdate(UpdateView):
    model= Desarrolladora
    success_url= "/Entregable/listaDesarrolladora"
    fields= ["nombre", "pais", "ciudad", "contacto", "imagen"]
    template_name= "Entregable/DesarrolladoraUpdate.html"

class DesarrolladoraDelete(DeleteView):
    model= Desarrolladora
    success_url= "/Entregable/listaDesarrolladora"
    template_name= "Entregable/DesarrolladoraConfirmDelete.html"

class DesarrolladoraCreate(CreateView):
    model= Desarrolladora
    success_url= "/Entregable/listaDesarrolladora"
    fields= ["nombre", "pais", "ciudad", "contacto", "imagen"]
    template_name= "Entregable/DesarrolladoraNew.html"





def crea_juego(request):

    if (request.method == "POST"):
        mi_formulario = FormJuego(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            juego = Juego(
                nombre = data["nombre"], 
                genero = data["genero"], 
                fechaDeLanzamiento = data["fechaDeLanzamiento"],
                plataforma = data["plataforma"],
                )
            juego.save()
            return render(request, "Entregable/Inicio.html")

    else:
        mi_formulario = FormJuego()

    return render(request, "Entregable/JuegoNuevo.html", {"form": mi_formulario})

def elimina_juego(request, id_juego):
    juego = Juego.objects.get(id=id_juego)

    juego.delete()

    lista_juegos = Juego.objects.all()

    return render(request, "Entregable/Juegos.html", {"lista": lista_juegos})

def crea_desarrolladora(request):

    if (request.method == "POST"):
        mi_formulario = FormDesarrolladora(request.POST)

        if (mi_formulario.is_valid()):
            data = mi_formulario.cleaned_data
            desarrolladora  = Desarrolladora(nombre = data["nombre"], 
                            apellido = data["apellido"], 
                            dni = data["dni"]
                            )
            desarrolladora.save()
            return render(request, "Entregable/Inicio.html")
            
    else:
        mi_formulario = FormDesarrolladora()

    return render(request, "Entregable/DesarrolladoraNuevo.html", {"form": mi_formulario})

def elimina_desarrolladora(request, id_desarrolladora):
    desarrolladora = Desarrolladora.objects.get(id=id_desarrolladora)

    desarrolladora.delete()

    lista_desarrolladoras = Desarrolladora.objects.all()

    return render(request, "Entregable/Desarrolladoras.html", {"lista": lista_desarrolladoras})






def busqueda_juego(request):
    return render(request, "Entregable/BusquedaJuego.html")
    
def buscar_juego(request):

    if request.GET["dni"]:

        dni = request.GET["dni"]
        juegos = Juego.objects.filter(dni__icontains=dni)

        return render(request, "Entregable/ResultadoBusquedaJuego.html", {"juegos": juegos, 'dni':dni})
    else:
        respuesta = "No enviaste datos"

    return render(request, 'Entregable/Inicio.html', {'respuesta': respuesta})

def busqueda_desarrolladora(request):
    return render(request, "Entregable/BusquedaDesarrolladora.html")

def buscar_desarrolladora(request):

        if(request.GET["dni"]):
            dni = request.GET["dni"]
            desarrolladoras = Desarrolladora.objects.filter(dni__icontains=dni)

            return render(request, "Entregable/ResultadoBusquedaDesarrolladora.html", {"desarrolladoras": desarrolladoras, "dni": dni})

        else:
            respuesta = "No enviaste datos"
        return HttpResponse(respuesta)






def editarPerfil(request):
    
    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)

        if (mi_formulario.is_valid()):

            data = mi_formulario.cleaned_data
            
            usuario.first_name = data['first_name']            
            usuario.last_name = data['last_name']
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]

            usuario.save()
        
            return render(request, "Entregable/Inicio.html")
            
    else:
        mi_formulario = UserEditForm(initial={"email": usuario.email})

        return render(request, "Entregable/EditarPerfil.html", {"form": mi_formulario, "usuario": usuario} )

@login_required
def agregarAvatar(request):

    user = str(User.objects.get(username=request.user))
    
    if user == "admin":
        if request.method == "POST":
            
            mi_formulario = AvatarForm(request.POST, request.FILES)

            if (mi_formulario.is_valid()):

                user = User.objects.get(username=request.user)

                avatar = Avatar(user=user, imagen=mi_formulario.cleaned_data['imagen'])
                avatar.save()

                return render(request, "Entregable/Inicio.html")
                
        else:
            mi_formulario = AvatarForm()

            return render(request, "Entregable/AgregarAvatar.html", {"form": mi_formulario} )
    else:
        return render(request, "Entregable/Inicio.html")

