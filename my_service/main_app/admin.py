from django.contrib import admin
from main_app.models import Glossary, GlossaryItem


@admin.register(Glossary)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'version', 'initial_date']


@admin.register(GlossaryItem)
class GlossaryItemAdmin(admin.ModelAdmin):
    list_display = ['article', 'ref_book']
