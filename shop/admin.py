from django.contrib import admin

from .models import Item

# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = ['price']
    list_display = ['__str__', 'price']