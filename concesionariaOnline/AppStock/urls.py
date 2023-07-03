from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('errorFiltradoCompra/',errorFiltradoCompra, name='errorFiltradoCompra'),
    path('compraFinalizada/',compraFinalizada, name='compraFinalizada'),
    path('autoPublicado/', autoPublicado, name='autoPublicado'),
    path('nosComunicaremos/',nosComunicaremos, name='nosComunicaremos'),
    path('servicios/', servicios, name='servicios'),
    path('sobreNosotros/', sobreNosotros, name='sobreNosotros'),
    path('compra/', listaDeCompra.as_view(), name='compra'),
    path('asesoramiento/', asesoramiento.as_view(), name='asesoramiento'),
    path('venta/', venta.as_view(), name='venta'),
    path('buscarCompra/', buscarCompra, name='buscarCompra'),
    path('detalleDelAuto/<pk>/', detalleDelAuto.as_view(), name='detalleDelAuto'),
    path('editarPublicacion/<pk>/', editarPublicacion.as_view(), name='editarPublicacion'),
    path('comprarAuto/<pk>/', comprarAuto.as_view(), name='comprarAuto'),
    path('iniciarSesion/', iniciarSesion, name='iniciarSesion'),
    path('registrar/', registrar, name='registrar'),
    path('cerrarSesion/', LogoutView.as_view(template_name= 'cerrarSesion.html'), name='cerrarSesion'),
    path('editarUsuario/', editarUsuario, name='editarUsuario'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('miCuenta/', miCuenta, name='infoCuenta'),
]
