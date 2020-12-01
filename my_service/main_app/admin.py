from django.contrib import admin
from main_app.models import Glossary, GlossaryItem, Version


class OrderItemInline(admin.TabularInline):
    model = Version
    raw_id_fields = ['glossary']


@admin.register(Glossary)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'id']
    inlines = [OrderItemInline]


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ['glossary', 'version', 'initial_date']


@admin.register(GlossaryItem)
class GlossaryItemAdmin(admin.ModelAdmin):
    list_display = ['article', 'ref_book']
