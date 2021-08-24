from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_code', 'type', 'description', 'photo','is_available', 'MW', 'material', 'age')
    list_display_links = ('id', 'model_code')
    search_fields = ('type', 'description', )
    list_editable = ('is_available',)
    list_filter = ('age', 'MW', 'material')


class YearAdmin(admin.ModelAdmin):
    list_display = ('id', 'year')
    list_display_links = ('id','year')
    search_fields = ('year',)
    list_filter = ('year',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Year, YearAdmin)

# admin.site.register(Category, CategoryAdmin)


#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#
