import re
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import Version, Glossary, GlossaryElement


def is_parameters_valid(id=None, slug=None, date=None, list_id=None):
    # проверка параметров
    try:
        if id == '0':
            return False
        elif id:
            int(id)
        if slug:
            slug_re = re.compile(r'^[-a-zA-Z0-9_.]+\Z', 0)
            validate_slug = RegexValidator(slug_re)
            validate_slug(slug)
            #validate_slug(slug)
        if date:
            datetime.strptime(date, '%Y-%m-%d')
        if list_id:
            [int(i) for i in list_id]
        return True
    except ValueError:
        return False
    except ValidationError:
        return False


def get_current_versions(date=datetime.now().date()):
    # вернуть актуальную версию словаря на указанную дату или на текущею
    return Version.objects.filter(initial_date__lte=date).order_by('glossary__id', '-initial_date') \
        .distinct('glossary__id')


def get_current_version(id):
    # вернуть текущую версию выбранного словаря, если нет то None
    date = datetime.now().date()
    return Version.objects.filter(initial_date__lte=date, glossary__id=id).order_by('-initial_date').last()


def get_elements_current_glossary(id):
    # вернуть элементы словаря текущей версии, если нет то None
    version = get_current_version(id)
    if version:
        return GlossaryElement.objects.filter(glossary_ver__id=version.id)


def get_elements_glossary_cpec_ver(id, version):
    # вернуть элементы выбранного справочника выбранной версии, если нет, то пустой qwerty_set
    return GlossaryElement.objects.filter(glossary_ver__glossary__id=id,
                                          glossary_ver__version=version)


def get_filtered_items(id, elements_list, version=None):

    current_version = get_current_version(id)
    return GlossaryElement.objects.filter(glossary_ver__id=current_version.id, id__in=elements_list)
