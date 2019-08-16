from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_view, name="home"),
    path("eventos/",views.ingreso_view, name="eventos"),
    path("login/",views.login_view, name="login"),
    path("registro/",views.registroUsuario_view, name="registro"),
    path("logout", views.logout_view, name="logout")
]