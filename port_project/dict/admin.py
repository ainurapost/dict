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
    list_display_links = ('id', 'year')
    search_fields = ('year',)
    list_filter = ('year',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_code', 'client_name', 'price', 'quantity', 'debt', 'created_at')
    list_display_links = ('id', 'model_code')
    search_fields = ('model_code', 'client_name' )
    list_editable = ('debt',)
    list_filter = ('model_code', 'client_name', 'created_at')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'info', 'is_debtor', 'client_debt')
    list_display_links = ('id', 'client_name')
    search_fields = ('info', 'client_name')
    list_editable = ('is_debtor', 'info')
    list_filter = ('client_name', 'is_debtor')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'feedback', 'owner')
    list_display_links = ('id', 'owner' )
    search_fields = ('owner', 'client_name')
    list_filter = ('owner',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)

admin.site.register(Feedback, FeedbackAdmin)

# admin.site.register(Category, CategoryAdmin)


#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#
