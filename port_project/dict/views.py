from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404

from .models import Product, Category, Color, Year, Client, Order

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    products = Product.objects.all()
    return render(request, 'dict/index.html', {'products': products, 'menu': menu, 'title': 'Главная страница'})


def new_order(request):
    return HttpResponse('Добавить заказ')


def login(request):
    return HttpResponse('Авторизация')


def all_categories(request):
    categories = Category.objects.all()
    years = Year.objects.all()
    colors = Color.objects.all()
    context = {
        'categories': categories,
        'years': years,
        'colors': colors,
        'menu': menu,
        'title': 'Категории'
    }
    return render(request, 'dict/all_categories.html', context=context)


def view_client(request, id):
    debt = 0
    client = get_object_or_404(Client, pk=id)
    # orders = Order.objects.filter(id=pk)

    return render(request, 'dict/view_client.html', {'client': client,})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page was not found</h1>')
