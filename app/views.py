from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Empleado, Producto
from django.contrib.auth.decorators import login_required
from .forms import EmpleadoForm
from .forms import ProductoForm

def home(request):
    return render(request, 'home.html') 

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and password2 and password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'error': 'El usuario ya existe.'
                })
        else:
            return render(request, 'signup.html', {
                'error': 'Las contraseñas no coinciden.'
            })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')
        
def signout(request):
    logout(request)
    return redirect('home')

@login_required  
def personal(request):
    empleados = Empleado.objects.filter(usuario=request.user)
    return render(request, 'personal/personal.html', {'empleados': empleados})

@login_required
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.usuario = request.user  
            empleado.save()
            return redirect('personal')
    else:
        form = EmpleadoForm()
    return render(request, 'personal/crear_empleado.html', {'form': form})

@login_required
def modificar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id, usuario=request.user)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('personal')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'personal/modificar_empleado.html', {'form': form, 'empleado': empleado})

@login_required
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id, usuario=request.user) 
    empleado.delete() 
    messages.success(request, "Empleado eliminado exitosamente.") 
    return redirect('personal') 
@login_required
def detalle_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    return render(request, 'personal/detalle_empleado.html', {'empleado': empleado})

@login_required
def producto(request):
    productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'producto/producto.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('producto') 
    else:
        form = ProductoForm()
    return render(request, 'producto/crear_producto.html', {'form': form})
