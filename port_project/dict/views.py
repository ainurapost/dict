from django.core.paginator import Paginator
from django.db.models import Q, Sum, Count, F, Min, Max
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from itertools import chain


from .forms import *


def landing(request):
    return render(request, 'dict/landing.html', {'title': 'Добро пожаловать!'})


@login_required(login_url='login')
def about(request):
    return render(request, 'dict/about.html', {'title': 'О нас'})

@login_required(login_url='login')
def index(request):
    products = Product.objects.all()
    p = Paginator(products, 3)
    page_no=request.GET.get('page')
    page_products= p.get_page(page_no)
    return render(request, 'dict/index.html', {'products': products, 'title': 'Главная страница', 'page_products': page_products})


@login_required(login_url='login')
def order(request):
    orders = Order.objects.all().order_by('-created_at')
    total= Order.objects.aggregate(total_debt=Sum(F('price') * F('quantity')))
    clear_total=total['total_debt']

    return render(request, 'dict/order.html', {'orders': orders, 'title': 'Лист заказов', 'clear_total': clear_total})


@login_required(login_url='login')
def orders_by_date(request, selected_date):
    orders = Order.objects.filter(created_at__date=selected_date)
    quantity_all_orders = len(orders)
    total_sales = Order.objects.filter(created_at__date=selected_date).aggregate(Sum('debt'))
    sales = total_sales.get('debt__sum')
    orders = Order.objects.filter(created_at__date=selected_date).filter()



    context = {
        'orders': orders,

        'selected_date': selected_date,
        'title': 'Заказы по дате',
        'quantity_all_orders': quantity_all_orders,
        'sales': sales
    }
    return render(request, 'dict/orders_by_date.html', context)


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
    return render(request, 'dict/register.html', context)


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
    return render(request, 'dict/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def view_client(request, id):
    client = get_object_or_404(Client, pk=id)
    orders = Order.objects.filter(client_name_id=id)
    quantity_orders = len(orders)
    debt = 0
    for order in orders:
        debt += order.debt


    context = {
        'client': client,
        'orders': orders,
        'total_debt': debt,
        'qty_orders': quantity_orders,

    }
    return render(request, 'dict/view_client.html', context=context)


@login_required(login_url='login')
def view_product(request, id):
    product = get_object_or_404(Product, pk=id)
    orders = Order.objects.filter(model_code_id=id)
    quantity_all_orders= len(Order.objects.all())
    total_sales = Order.objects.all().aggregate(Sum('debt'))

    quantity_orders = len(orders)
    sales = 0
    for order in orders:
        sales += order.debt
    total_sales.get('debt__sum')

    qs_max = Product.objects.filter(id=id).annotate(Max('order__price'))
    qs_min = Product.objects.filter(id=id).annotate(Min('order__price'))
    max_price = vars(qs_max[0])['order__price__max']
    min_price = vars(qs_min[0])['order__price__min']


    share = quantity_orders/quantity_all_orders*100
    share2 = sales/total_sales.get('debt__sum')*100
    share2 = '{:0.2f}'.format(share2)

    context = {
        'product': product,
        'orders': orders,
        'title': f'Товар:{id}',
        'qty_orders': quantity_orders,
        'sales': sales,
        'share': share,
        'share2': share2,
        'max_price': max_price,
        'min_price': min_price,
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
def get_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            owner = form.cleaned_data.get('owner')
            messages.success(request, 'Ваше обращение: ' + owner + ' успешно зарегистрировано')
            return redirect('home')

    else:
        form = FeedbackForm()
    return render(request, 'dict/feedback.html', {'form': form, 'title': 'Обратаная связь'})


@login_required(login_url='login')
def search(request):

    query = request.GET.get('query')
    if request.GET.get('query') is None:
        return render(request, 'dict/search.html')

    res1 = Product.objects.filter(Q(model_code__icontains=request.GET.get('query')) |
                                 Q(description__icontains=request.GET.get('query')) |
                                 Q(type__icontains=request.GET.get('query')))

    res2 = Client.objects.filter(Q(client_name__icontains=request.GET.get('query')) |
                                 Q(info__icontains=request.GET.get('query')))


    res = list(chain(res1, res2))
    print(res)
    return render(request, 'dict/search.html', {'result': res, 'title': 'Поиск'})


