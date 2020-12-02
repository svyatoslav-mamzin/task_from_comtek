from django.contrib import admin
from .models import Glossary, GlossaryElement, Version


class VersionInline(admin.TabularInline):
    model = Version
    raw_id_fields = ['glossary']


class ElementInline(admin.TabularInline):
    model = GlossaryElement
    raw_id_fields = ['glossary_ver']


@admin.register(Glossary)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'id']
    inlines = [VersionInline]


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ['glossary', 'version', 'initial_date']
    inlines = [ElementInline]


@admin.register(GlossaryElement)
class GlossaryElementAdmin(admin.ModelAdmin):
    list_display = ['article', 'glossary_ver']
