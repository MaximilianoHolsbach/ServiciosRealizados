from django.urls import path
from Bitacora import views

urlpatterns = [
    path("", views.Bitacorainicio.as_view(), name="Bitacorainicio"),
    path("log/", views.BitacoraLogin.as_view(), name="BitacoraLogin"),
    path("Crear/", views.BitacoraCreate.as_view(), name="BitacoraCreate"),
    path('listar/', views.BitacoraList.as_view(), name = "BitacoraList"),
    path("detalle/<pk>/", views.BitacoraDetail.as_view(), name ="BitacoraDetail"),
    path("editar/<pk>/", views.BitacoraUpdate.as_view(), name ="BitacoraUpdate"),
    path("borrar/<pk>/", views.BitacoraDelete.as_view(), name ="BitacoraDelete"),
    path("crear-cuenta/", views.SignUpView.as_view(), name ="Bitacorasignup"),
    path("salir/", views.BlogLogout.as_view(), name="Bitacoralogout"),
    
]