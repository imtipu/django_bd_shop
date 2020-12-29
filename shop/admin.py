from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'handle', 'price', 'created', 'updated']
    readonly_fields = ['handle']

    search_fields = ['title', 'handle', 'price']
