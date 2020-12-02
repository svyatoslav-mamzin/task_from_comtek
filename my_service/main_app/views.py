from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Glossary
from .models import GlossaryElement
from .serializers import GlossarySerializer, ElementsGlossarySerializer
from .servises import date_validation


class GlossaryView(APIView):
    # получение списка справочников
    def get(self, request):
        glossaries = Glossary.objects.all()
        serializer = GlossarySerializer(glossaries, many=True)
        return Response({"glossaries": serializer.data})


class CurrentGlossariesView(APIView):
    # получение списка справочников актуальных на указанную дату.
    def get(self, request, date):
        data = date_validation(date)
        if data:
            glossaries = Glossary.objects.filter(version__initial_date__lte=data)
            if glossaries:
                serializer = GlossarySerializer(glossaries, many=True)
                return Response({"current glossaries": serializer.data})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ElementsGlossarySpecVersView(APIView):
    # получение элементов заданного справочника указанной версии
    def get(self, request, id, version):
        # is valid id and version дописать!!!
        elements = GlossaryElement.objects.filter(glossary_ver__glossary__id=id,
                                                  glossary_ver__version=version)
        if elements:
            serializer = ElementsGlossarySerializer(elements, many=True)
            return Response({"Elements Glossary Spec Vers": serializer.data})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
