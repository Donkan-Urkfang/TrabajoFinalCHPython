from django.urls import path
from Entregable import views
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path("pages/", views.paginas, name="paginas"),

    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='Entregable/Login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Entregable/Logout.html'), name='logout'),

    path("editarPerfil/", views.editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", views.agregarAvatar, name="agregarAvatar"),  
    path("buscarJuego/", views.buscar_juego, name="buscarJuego"),
    path("buscarDesarrolladora/", views.buscar_desarrolladora, name="buscarDesarrolladora"),
    path("busquedaJuego/", views.busqueda_juego, name="busquedaJuego"),
    path("busquedaDesarrolladora/", views.busqueda_desarrolladora, name="busquedaDesarrolladora"),
    path("eliminarJuego/<id_juego>/", views.elimina_juego, name="eliminaJuego"),
    path("Juegos/", views.juegos, name="juegos"),
    path("listaJuego/", views.JuegoList.as_view(), name="VistaJuego"),
    path("detalleJuego/<pk>/", views.JuegoDetail.as_view(), name="DetailJuego"),
    path("actualizaJuego/<pk>/", views.JuegoUpdate.as_view(), name="EditJuego"),
    path("eliminaJuego/<pk>/", views.JuegoDelete.as_view(), name="DeleteJuego"),
    path("crearJuego/", views.JuegoCreate.as_view(), name="NewJuego"),
    path("listaDesarrolladora/", views.DesarrolladoraList.as_view(), name="VistaDesarrolladora"),
    path("detalleDesarrolladora/<pk>/", views.DesarrolladoraDetail.as_view(), name="DetailDesarrolladora"),
    path("actualizaDesarrolladora/<pk>/", views.DesarrolladoraUpdate.as_view(), name="EditDesarrolladora"),
    path("eliminaDesarrolladora/<pk>/", views.DesarrolladoraDelete.as_view(), name="DeleteDesarrolladora"),
    path("crearDesarrolladora/", views.DesarrolladoraCreate.as_view(), name="NewDesarrolladora"),

]   
