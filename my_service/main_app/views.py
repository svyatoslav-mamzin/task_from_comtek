from django.http import HttpResponse
from django.shortcuts import render


from main_app.models import Glossary


def glossary_list(request):
    glossaries = Glossary.objects.all()
    for item in glossaries:
        print(item.id, item.name, item.version)

    return HttpResponse('Invalid login')