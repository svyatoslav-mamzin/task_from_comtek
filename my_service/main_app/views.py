from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Glossary
from .serializers import GlossarySerializer, ElementsGlossarySerializer, VersionsSerializer
from .servises import date_validation, get_current_versions, get_elements_current_glossary, \
    get_elements_glossary_cpec_ver, validate_parameters


class GlossaryView(APIView):
    # получение списка справочников
    def get(self, request):
        glossaries = Glossary.objects.all()
        serializer = GlossarySerializer(glossaries, many=True)
        return Response({"glossaries": serializer.data})


class CurrentGlossariesView(APIView):
    # получение списка справочников актуальных на указанную дату.
    def get(self, request, date):

        if validate_parameters(date=date):
            glossaries = get_current_versions(date)
            if glossaries:
                serializer = VersionsSerializer(glossaries, many=True)
                return Response({"current glossaries": serializer.data})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ElementsGlossaryCurrentVersView(APIView):
    # получение элементов заданного справочника текущей версии
    def get(self, request, id):
        if validate_parameters(id=id):
            elements = get_elements_current_glossary(id)
            if elements:
                serializer = ElementsGlossarySerializer(elements, many=True)
                return Response({"Elements Glossary Current Version": serializer.data})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ElementsGlossarySpecVersView(APIView):
    # получение элементов заданного справочника указанной версии
    def get(self, request, id, version):
        if validate_parameters(id=id, slug=version):
            elements = get_elements_glossary_cpec_ver(id, version)
            if elements:
                serializer = ElementsGlossarySerializer(elements, many=True)
                return Response({"Elements Glossary Spec Vers": serializer.data})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
