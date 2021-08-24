from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Client, Order, Category, Year, Material, AGE
from .forms import *


@login_required(login_url='login')
def index(request):
    products = Product.objects.all()
    return render(request, 'dict/index.html', {'products': products, 'title': 'Главная страница'})

@login_required(login_url='login')
def new_order(request):
    return HttpResponse('Добавить заказ')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Регистрация успешно проведена для ' + user)
                return redirect('login')

    context = {'form': form, 'title': 'Регистрация'}
    return render(request,'dict/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Имя пользователя или пароль неверны')
    context = {'title': 'Войти'}
    return render(request,'dict/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def view_client(request, id):
    debt = 0
    client = get_object_or_404(Client, pk=id)
    # orders = Order.objects.filter(id=pk)

    return render(request, 'dict/view_client.html', {'client': client, })


@login_required(login_url='login')
def view_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
        'title': f'Product:{id}',
    }

    return render(request, 'dict/view_product.html', context=context)


@login_required(login_url='login')
def view_wm(request, category_id):
    products = Product.objects.filter(MW_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'dict/view_wm.html', {'products': products, 'category': category,
                                                 })


@login_required(login_url='login')
def view_year(request, year_id):
    products = Product.objects.filter(year_id=year_id)
    years = Year.objects.get(pk=year_id)
    return render(request, 'dict/view_year.html', {'products': products, 'years': years, })


@login_required(login_url='login')
def view_material(request, material_id):
    products = Product.objects.filter(material_id=material_id)
    materials = Material.objects.get(pk=material_id)
    return render(request, 'dict/view_material.html', {'products': products, 'materials': materials, })


@login_required(login_url='login')
def view_age(request, age_id):
    products = Product.objects.filter(age_id=age_id)
    ages = AGE.objects.get(pk=age_id)
    return render(request, 'dict/view_age.html', {'products': products, 'ages': ages, })


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page was not found</h1>')


@login_required(login_url='login')
def new_client(request):
    if request.method == 'POST':
        form = NewClientForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = NewClientForm()
    return render(request, 'dict/new_client.html', {'form': form, 'title': 'Добавить клиента'})


@login_required(login_url='login')
def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = NewProductForm()
    return render(request, 'dict/new_product.html', {'form': form, 'title': 'Добавить товар'})