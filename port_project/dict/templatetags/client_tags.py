from django import template

from dict.models import Client, Category, AGE, Material, Year

register = template.Library()


@register.simple_tag(name='get_client_list')
def get_clients():
    return Client.objects.all()


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

