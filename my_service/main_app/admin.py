from django.contrib import admin

# Register your models here.
from main_app.models import ReferenceBook, RefBookItem


@admin.register(ReferenceBook)
class CartAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'version', 'initial_date']


@admin.register(RefBookItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ['article', 'ref_book']
