from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('home/', index, name='home'),
    path('', landing, name='landing'),
    path('orders/', order, name='order'),
    path('orders_by_date/<selected_date>', orders_by_date, name='orders_by_date'),
    # url(r'^orders_by_date/(?P<selected_date>\d{4}-d{2}-d{2})/$', orders_by_date, name='orders_by_date'),
    path('new_order/', new_order, name='new_order'),
    path('new_client/', new_client, name='new_client'),
    path('new_product/', new_product, name='new_product'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', register, name='register'),
    path('view_client/<int:id>', view_client, name='view_client'),
    path('view_product/<int:id>', view_product, name='view_product'),
    path('view_wm/<int:category_id>', view_wm, name='view_wm'),
    path('view_year/<int:year_id>', view_year, name='view_year'),
    path('view_material/<int:material_id>', view_material, name='view_material'),
    path('view_age/<int:age_id>', view_age, name='view_age'),
    path('search/', search, name='search'),

    ]
