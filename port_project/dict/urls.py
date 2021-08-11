from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('new_order/',new_order, name='new_order'),
    path('login/', login, name='login'),
    path('all_categories/', all_categories, name='all_categories'),
    path('view_client/<int:id>', view_client, name='view_client'),

    ]



