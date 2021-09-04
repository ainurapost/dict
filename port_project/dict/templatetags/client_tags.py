from django import template

from dict.models import Client, Category, AGE, Material, Year, Product, Order

register = template.Library()


@register.simple_tag(name='get_order_dates')
def get_dates():
    return Order.objects.dates('created_at','day', order='DESC')


@register.simple_tag(name='get_client_list')
def get_clients():
    return Client.objects.all()

@register.simple_tag(name='get_product_list')
def get_product():
    return Product.objects.all()

@register.simple_tag(name='get_age_category')
def get_age_category():
    return AGE.objects.all()


@register.simple_tag(name='get_wm_category')
def get_wm_category():
    return Category.objects.all()

@register.simple_tag(name='get_material_category')
def get_material_category():
    return Material.objects.all()

@register.simple_tag(name='get_year_category')
def get_year_category():
    return Year.objects.all()

@register.simple_tag(name='get_product_by_order')
def get_product_by_order(product_id):
    product = Product.objects.get(pk=product_id)
    return product.order_set.all()
