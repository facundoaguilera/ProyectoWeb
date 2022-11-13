from email import message
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

# def autenticacion(request):
#     return render(request, 'registro/registro.html')
class VRegistro(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,'registro/registro.html',{'form':form})
        
    def post(self,request):
        form=UserCreationForm(request.POST) #almaceno todo lo que hay en el formulario
        if form.is_valid():
            usuario=form.save() #variable para guardar los datos en las bases de datos
            login(request,usuario) #creo un login

            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,'registro/registro.html',{'form':form})
def cerrarSesion(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method == 'POST': #si pulso el boton de Login
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contrasenia=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario,password=contrasenia)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request,'usuario no valido')
        else:
            messages.error(request,'informacion no valida')
    form=AuthenticationForm
    return render(request, 'login/login.html',{'form':form})

    
        
