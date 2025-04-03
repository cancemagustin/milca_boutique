from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegistroForm
from .models import Perfil

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # Crear el perfil vinculado al usuario
            perfil = form.save(commit=False)
            perfil.usuario = user
            perfil.save()

            # Iniciar sesión automáticamente
            login(request, user)

            return redirect('Main:home')
    else:
        form = RegistroForm()

    return render(request, 'Perfil/registrar.html', {'form': form})