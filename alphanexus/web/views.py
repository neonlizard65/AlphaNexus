from django.forms import ValidationError
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, EditUserForm
from .models import CustomUser

def index(request):
    context = {"n": range(0, 20)}
    return render(request, "index.html", context=context)

def about(request):
    return render(request, "about.html")

def register(request: HttpRequest):
    form = RegisterForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            messages.success(request, "Успешная регистрация")
            login(request, user)
            return redirect("home")
    return render(request, "register.html", context = {"form": form})

def user_login(request: HttpRequest):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST) 
        if form.is_valid():
            user = form.get_user()
            if user is not None and user.is_active:
                login(request, user)
                return redirect("home")
            messages.error(request, "Неверно указана почта или пароль")
            return render(request, "login.html", context={"form": form})      
        messages.error(request, "Неверно указана почта или пароль")
        return render(request, "login.html", context={"form": form})
    form = AuthenticationForm()
    return render(request, "login.html", context={"form": form})

#Личный кабинет (нужно быть авторизованным, иначе редирект на login)
@login_required(login_url='/login')
def cabinet(request: HttpRequest):
    user_data = CustomUser.objects.get(id = request.user.id)
    context = {'user': user_data}
    return render(request, 'cabinet.html', context)
    
@login_required(login_url='/login')
def change_user(request: HttpRequest):
    user_data = CustomUser.objects.get(id = request.user.id)
    context = {'user': user_data}
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
                messages.success(request, 'Учётная запись обновлена')
                user = form.save()
                return render(request, "change_user.html", context = {'form': form, 'data': user_data})
        else:
                return render(request, "change_user.html", context = {'form': form, 'data': user_data})
    else: 
        form = EditUserForm(instance = request.user)
        return render(request, "change_user.html", context = {'form': form, 'data': user_data})



#Изменение пароля в личном кабинете
@login_required(login_url='/login')
def change_password(request: HttpRequest):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Пароль обновлен!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

#TODO: Забыли пароль?

#Изменение пароля в личном кабинете
@login_required(login_url='/login')
def library(request: HttpRequest):
    return render(request, 'library.html')

def store(request: HttpRequest):
    return render(request, 'store.html')

def user_logout(request):
    logout(request)
    return redirect("home")

def page404(request, exception):
    return render(request, '404.html', status=404)

def developer(request):
    return render(request, "developer.html")