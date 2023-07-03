from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):

        return render(request, 'inicio.html')

def errorFiltradoCompra(request):

    return render(request, 'errorFiltradoCompra.html')

def compraFinalizada(request):

    return render(request, 'compraFinalizada.html')

@login_required
def miCuenta(request):

    try:
        avatar= Avatar.objects.get(user= request.user.id)
        return render( request, 'miCuenta.html', {'url': avatar.imagen.url})
    except:
        return render(request, 'miCuenta.html')

def autoPublicado(request):

    return render(request, 'autoPublicado.html')

def nosComunicaremos(request):

    return render(request, 'nosComunicaremos.html')
class venta (LoginRequiredMixin, CreateView):
    model = Autos
    template_name = "venta.html"
    fields= ('__all__')
    success_url= '/app-stock/autoPublicado'
    
class asesoramiento (LoginRequiredMixin, CreateView):
    model = Asesoramiento
    template_name = "asesoramiento.html"
    fields= ('__all__')
    success_url= '/app-stock/nosComunicaremos/'

def servicios(request):

    return render(request, 'servicios.html')

def sobreNosotros(request):

    return render(request, 'sobreNosotros.html')
class listaDeCompra (ListView):
    model= Autos
    template_name='compra.html'
    context_object_name='listadoDeAutos'
    def compra(request):
        return render( request, 'compra.html', {'url': Autos.imagen.url})

def buscarCompra(request):

    if request.GET['modelo']:

        marca= request.GET['modelo']
        autos= Autos.objects.filter(marca=marca)

        return render(request, 'resultadoDeBusqueda.html',{'autos': autos, 'marca': marca})
    else:
        return render(request, 'errorFiltradoCompra.html')
class detalleDelAuto(DetailView):
    model = Autos
    template_name = "detalleAuto.html"
    context_object_name= 'auto'
class comprarAuto(LoginRequiredMixin,DeleteView):
    model = Autos
    context_object_name= 'auto'
    template_name = "comprarAuto.html"
    success_url= '/app-stock/compraFinalizada/'

class editarPublicacion(LoginRequiredMixin,UpdateView):
    model = Autos
    template_name = "editarPublicacion.html"
    fields= ('__all__')
    success_url= '/app-stock/compra/'
    context_object_name='auto'

def iniciarSesion(request):

    if request.method == 'POST':
        miFormulario = AuthenticationForm(request, data = request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            contrasenia = data["password"]
      
            cuentaUsuario = authenticate(username = usuario, password = contrasenia)

            if cuentaUsuario:
                login(request, cuentaUsuario)
                return render(request, 'inicio.html')
            else:
                return render(request, 'errorIniciarSesion.html')
        else:
            return render(request, "errorIniciarSesion.html")
    else:
        miFormulario = AuthenticationForm()
        return render(request, "iniciarSesion.html", {"miFormulario": miFormulario})
    
def registrar(request):
    
    if request.method == 'POST':
        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(request, 'usuarioCreado.html', {"mensaje": usuario})

        else:
            return render(request, "errorIniciarSesion.html")
    else:
        miFormulario = UserCreationForm()
        return render(request, "registrar.html", {"miFormulario": miFormulario})
 
@login_required   
def editarUsuario(request):

    usuario = request.user

    if request.method == 'POST':
      
        miFormulario = EditarUsuario(request.POST, instance= request.user)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.email = data['email']
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.set_password(data["password1"])
            usuario.save()
            
            return render(request, "usuarioEditado.html")
        else:
            return render(request, "errorIniciarSesion.html", {"miFormulario": miFormulario})
    else:
        miFormulario = EditarUsuario(instance=request.user)
        return render(request, "editarUsuario.html", {"miFormulario": miFormulario})

@login_required 
def agregarAvatar(request):

  if request.method == 'POST':
    miFormulario = AvatarFormulario(request.POST, request.FILES)

    if miFormulario.is_valid():
        
      data = miFormulario.cleaned_data
      avatar = Avatar(user=request.user, imagen=data["imagen"])
      avatar.save()

      return render(request, 'inicio.html')
         
    else:
      return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
  
  else:
    miFormulario = AvatarFormulario()
    try:
       avatarYaCargado= Avatar.objects.get(user= request.user.id)
       return render( request, 'agregarAvatar.html', {"miFormulario": miFormulario,'url': avatarYaCargado.imagen.url})
    except:
       return render(request, 'agregarAvatar.html', {"miFormulario": miFormulario})
    