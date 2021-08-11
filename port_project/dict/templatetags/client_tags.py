from django import template

from dict.models import Client

register = template.Library()


@register.simple_tag(name='get_client_list')
def get_clients():
    return Client.objects.all()
