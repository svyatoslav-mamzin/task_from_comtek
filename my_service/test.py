from datetime import datetime
import os
import django
from django.core.validators import validate_slug

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_service.settings')
django.setup()
from main_app.models import Glossary, Version
from main_app.servises import get_current_version, get_elements_current_glossary

#date = input("enter date: ")

#glossaries = Glossary.objects.filter(version__initial_date__lte=date)
#glossaries2 = Glossary.objects.filter(version__initial_date__gte=date)
#glossaries = glossaries.intersection(glossaries2)
#versions = Version.objects.filter(initial_date__lte=date).order_by('glossary__id', '-initial_date').distinct('glossary__id')
#glossaries = Glossary.objects.filter(version__initial_date__lte=date)
#reverse('id').distinct('id').
#glossaries = Glossary.objects.filter(version__initial_date__lte=date)
#.latest('pub_date')
id=6
print(get_current_version(id))
print()
print(get_elements_current_glossary(id))
#qwerty_list = list()
#for glossary in Version.objects.filter(initial_date__lte=date).latest('initial_date'):
    #for ver in glossary.version:
#    print(glossary)
#    qwerty_list.append(glossary)
#print(qwerty_list)
validate_slug("%71!")



