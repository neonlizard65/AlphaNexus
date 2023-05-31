import logging
from math import e
import pdb
from urllib.request import Request;
from django.forms import ValidationError
from django.http import Http404, HttpRequest, HttpResponse, QueryDict
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import DeveloperForm, ProductForm, RegisterForm, EditUserForm
from .models import CustomUser, Developer, DeveloperRequest, Library, Product

def index(request:HttpRequest):
    
    products = Product.objects.all().order_by('-id')[:30]
    context = {"products": products}
    if(request.user.is_authenticated):
        user_data = CustomUser.objects.get(id = request.user.id)
        
        wishes_query = user_data.wishlist.all().values('id')
        wishes = []
        for dictionary in wishes_query:
            for key in dictionary:
                wishes.append(dictionary[key])
                
        cart_query = user_data.cart.all().values('id')
        cart = []
        for dictionary in cart_query:
            for key in dictionary:
                cart.append(dictionary[key])
                
        library_query = Library.objects.filter(user=user_data).values('product')  
        library = []
        for dictionary in library_query:
            for key in dictionary:
                library.append(dictionary[key]) 
                
        context = {"products": products, "user": user_data, "wishes": wishes, "cart": cart, "library": library}
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
                form.save()
                user_data = CustomUser.objects.get(id = request.user.id)
                return redirect(request.path_info)
        else:
                return render(request, "change_user.html", context = {'form': form, 'data': user_data})
    else: 
        user_data = CustomUser.objects.get(id = request.user.id)
        context = {'user': user_data}
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


def store(request: HttpRequest):
    products = Product.objects.all()
    context = {"products": products}
    if request.user.is_authenticated:
        user_data = get_object_or_404(CustomUser, id=request.user.id)
        
        wishes_query = user_data.wishlist.all().values('id')
        wishes = []
        for dictionary in wishes_query:
            for key in dictionary:
                wishes.append(dictionary[key])
                
        cart_query = user_data.cart.all().values('id')
        cart = []
        for dictionary in cart_query:
            for key in dictionary:
                cart.append(dictionary[key])
        
        library_query = Library.objects.filter(user=user_data).values('product')  
        library = []
        for dictionary in library_query:
            for key in dictionary:
                library.append(dictionary[key]) 
                
        context = {"user": user_data, "products": products, "wishes": wishes, "cart": cart, "library": library}
    return render(request, "store.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")

def page404(request, exception):
    return render(request, '404.html', status=404)


def developer(request:HttpRequest):
    if request.user.is_authenticated:
        user_data = CustomUser.objects.get(id = request.user.id)
        developer = Developer.objects.filter(creator = user_data).first()
        products = Product.objects.filter(developer = developer)
        requests = list(DeveloperRequest.objects.filter(user = user_data).values_list("developer"))
        if not developer:
            #Если пользователь не привязан к группе
            devs = Developer.objects.all()
            if requests:
                requests = [request[0] for request in requests]
                context = {'user': user_data, "developer":developer, "devs":devs, "products":products, "requests": requests}
            else:
                context = {'user': user_data, "developer":developer, "devs":devs, "products":products}        
            return render(request, "developer.html", context=context)   
        else:
            #Если пользователь привязан к группе
            context = {'user': user_data, "developer":developer, "products":products}
            return render(request, "developer.html", context=context)
    else:
        devs = Developer.objects.all()
        context = {"devs":devs}
        return render(request, "developer.html", context=context)


def developer_games(request:HttpRequest, id):
    developer = get_object_or_404(Developer, id=id)
    products = Product.objects.filter(developer = developer).distinct()
    users = CustomUser.objects.filter(developer = developer)
    if request.user.is_authenticated:
        user_data = CustomUser.objects.get(id = request.user.id)

        wishes_query = user_data.wishlist.all().values('id')
        wishes = []
        for dictionary in wishes_query:
            for key in dictionary:
                wishes.append(dictionary[key])
                
        cart_query = user_data.cart.all().values('id')
        cart = []
        for dictionary in cart_query:
            for key in dictionary:
                cart.append(dictionary[key])
                
        library_query = Library.objects.filter(user=user_data).values('product')  
        library = []
        for dictionary in library_query:
            for key in dictionary:
                library.append(dictionary[key]) 
        
        requests = list(DeveloperRequest.objects.filter(user = user_data).values_list("developer"))
        if requests:
            requests = [request[0] for request in requests]
            context = {"developer": developer, "products": products, "users": users, "requests": requests, "wishes": wishes, "cart": cart, "library": library}
        else:
            context = {"developer": developer, "products": products, "users": users, "wishes": wishes, "cart": cart, "library": library}
    else:
        context = {"developer": developer, "products": products, "users": users}
    
    return render(request, "developer_games.html" ,context)


def create_developer(request:HttpRequest):
    if request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES)
        context = {"form": form}
        if form.is_valid():
            user = CustomUser.objects.get(id = request.user.id)
            form.save(user=user)
            return redirect("developer")
        else:
            return render(request, "create_developer.html", context=context)
    else:
        form = DeveloperForm()
        context = {"form": form}
        return render(request, "create_developer.html", context=context)

@login_required(login_url='/login')
def change_product(request:HttpRequest, id):
    product = get_object_or_404(Product, id=id)
    user = get_object_or_404(CustomUser, id = request.user.id)
    if user.developer == product.developer:
        form = ProductForm(instance=product)
        context = {"product": product, "form": form}
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect(request.path_info)   
            else:
                return render(request, "change_product.html", context=context)    
        return render(request, "change_product.html", context=context)
    else:
        return HttpResponse("Unauthorized", status=401)
    
def create_product(request: HttpRequest):
    if request.method == 'POST':
        user = CustomUser.objects.get(id = request.user.id)
        form = ProductForm(request.POST, request.FILES)
        context = {"form": form}
        if form.is_valid():
            print(user.developer)
            form.save(user.developer)
            return redirect("developer")   
        else:
            return render(request, "create_product.html", context=context)    
    else:
        form = ProductForm()
        context = {"form": form}
        return render(request, "create_product.html", context=context)


def users(request:HttpRequest, id):
    user = get_object_or_404(CustomUser, id=id)
    context = {"user": user}
    return render(request, "users.html", context=context)

def product(request:HttpRequest, id):
    product = get_object_or_404(Product, id=id)
    context = {"product": product}
    
    if(request.user.is_authenticated):
        user_data = get_object_or_404(CustomUser, id=request.user.id)  

        wishes_query = user_data.wishlist.all().values('id')
        wishes = []
        for dictionary in wishes_query:
            for key in dictionary:
                wishes.append(dictionary[key])
                
        cart_query = user_data.cart.all().values('id')
        cart = []
        for dictionary in cart_query:
            for key in dictionary:
                cart.append(dictionary[key])
                
        library_query = Library.objects.filter(user=user_data).values('product')  
        library = []
        for dictionary in library_query:
            for key in dictionary:
                library.append(dictionary[key])         
        
        context = {"product": product, "user": user_data, "wishes": wishes, "cart": cart, "library": library}
        
    return render(request, "product.html", context)



@login_required(login_url="/login")
def wishlist(request):
    user_data = get_object_or_404(CustomUser, id=request.user.id)
    wishes_query = user_data.wishlist.all().values('id')
    wishes = []
    for dictionary in wishes_query:
        for key in dictionary:
            wishes.append(dictionary[key])
    cart_query = user_data.cart.all().values('id')
    cart = []
    for dictionary in cart_query:
        for key in dictionary:
            cart.append(dictionary[key])
    context = {"user": user_data, "wishes": wishes, "cart": cart}
    return render(request, "wishlist.html", context)



@login_required(login_url="/login")
def cart(request: HttpRequest):
    user_data = get_object_or_404(CustomUser, id=request.user.id)
    
    #wishlist
    wishes_query = user_data.wishlist.all().values('id')
    wishes = []
    for dictionary in wishes_query:
        for key in dictionary:
            wishes.append(dictionary[key])
        
    #cart
    cart_query = user_data.cart.all().values('id')
    cart = []
    for dictionary in cart_query:
        for key in dictionary:
            cart.append(dictionary[key])
    
    #sum
    prices = list(user_data.cart.all().values_list("price"))
    sum = 0
    for price in prices:
        sum += price[0]
    
    
    context = {"user": user_data, "wishes": wishes, "cart": cart, "sum": sum}
    return render(request, "cart.html", context)



@login_required(login_url='/login')
def library(request: HttpRequest):
    library = Library.objects.filter(user = request.user.id)
    context = {"library": library}
    
    return render(request, 'library.html', context=context)