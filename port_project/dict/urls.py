from django.urls import path, re_path
from .views import *
from .forms import *

urlpatterns = [
    path('', index, name='home'),
    path('new_order/',new_order, name='new_order'),
    path('new_client/',new_client, name='new_client'),
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

    ]





