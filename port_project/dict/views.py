from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


@login_required(login_url='login')
def index(request):
    products = Product.objects.all()
    return render(request, 'dict/index.html', {'products': products, 'title': 'Главная страница'})

@login_required(login_url='login')
def order(request):
    orders = Order.objects.all()
    return render(request, 'dict/order.html', {'orders': orders, 'title': 'Лист заказов'})


@login_required(login_url='login')
def new_order(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = NewOrderForm()
    return render(request, 'dict/new_order.html', {'form': form, 'title': 'Новый заказ'})


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
    client = get_object_or_404(Client, pk=id)
    orders = Order.objects.filter(client_name_id=id)
    debt=0
    for order in orders:
        debt += order.debt

    context = {
        'client': client,
        'orders': orders,
        'total_debt': debt
        }
    return render(request, 'dict/view_client.html', context=context)

@login_required(login_url='login')
def view_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
        'title': f'Товар:{id}',

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
            client = form.cleaned_data.get('client_name')
            messages.success(request, 'Клиент: ' + client + ' успешно внесен в базу данных')
            return redirect('home')

    else:
        form = NewClientForm()
    return render(request, 'dict/new_client.html', {'form': form, 'title': 'Добавить клиента'})


@login_required(login_url='login')
def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product = form.cleaned_data.get('model_code')
            messages.success(request, 'Модель: ' + product + ' успешно внесена в базу данных')
            return redirect('home')

    else:
        form = NewProductForm()
    return render(request, 'dict/new_product.html', {'form': form, 'title': 'Добавить товар'})


@login_required(login_url='login')
def new_order(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        if form.is_valid():
            form.save()
            # neworder = form.cleaned_data.get('pk')
            client = form.cleaned_data.get('client_name')
            # messages.success(request, 'Заказ ' +' для клиента ' + client + ' успешно внесен в базу данных')
            return redirect('order')

    else:
        form = NewOrderForm()
    return render(request, 'dict/new_order.html', {'form': form, 'title': 'Добавить заказ'})


@login_required(login_url='login')
def search(request):

    query = request.GET.get('query')
    if request.GET.get('query') is None:
        return render(request, 'dict/search.html')

    res = Product.objects.filter(Q(model_code__icontains=request.GET.get('query')) |
                              Q(description__icontains=request.GET.get('query')))
    return render(request, 'dict/search.html', {'result': res, 'title': 'Поиск'})