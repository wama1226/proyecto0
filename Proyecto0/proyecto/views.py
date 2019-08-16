from django.contrib.auth import authenticate, login, logout, hashers
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import RegistroUsuario,evento_form
from .models import Usuario,Evento
from django.contrib.auth.models import User

# Create your views here.
def index_view(request):
    if not request.user.is_authenticated:
        return render(request, "proyecto/login.html")
    context= {
        "user": request.user
    }
    return render(request, "proyecto/eventos.html", context,{'form':evento_form()})

def registroUsuario_view(request):
    submitted = False
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            #form.save()
            user = User.objects.create_user(request.POST['nombres'] ,request.POST['email'] ,request.POST['contrasena'])
            user.first_name = request.POST['nombres']
            user.last_name = request.POST['apellidos']
            user.save()
            return request('/registro/?submitted=True')
    else:
        form = RegistroUsuario()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'proyecto/registro.html', {'form': form, 'submitted': submitted})

def login_view(request):
    return render(request, "proyecto/login.html")

def ingreso_view(request):
    email=request.POST["email"]
    password=request.POST["password"]
    try:#para que la excepción se realice se debe usar el user.objects dentro del try
        u = User.objects.get(email=email)
        user = authenticate(request, username=u.username, password=password)
        if hashers.check_password(password,u.password):
            login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "proyecto/login.html", {"message": "Contraseña incorrecta"})
    except User.DoesNotExist:
        return render(request, "proyecto/login.html", {"message": "Credenciales invalidas"})

def logout_view(request):
    logout(request)
    return render(request, "proyecto/login.html", {"message": "Logged out."})