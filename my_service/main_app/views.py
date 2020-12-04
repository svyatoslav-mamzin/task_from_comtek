from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Glossary
from .serializers import GlossarySerializer, ElementsGlossarySerializer, VersionsSerializer
from .servises import get_current_versions, get_elements_current_glossary, \
    get_elements_glossary_cpec_ver, is_parameters_valid
from my_service.pagination import MyPaginationMixin
from rest_framework.settings import api_settings


class GlossaryView(APIView, MyPaginationMixin):
    # получение списка справочников
    queryset = Glossary.objects.all()
    serializer_class = GlossarySerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response({"glossaries": serializer.data})


class CurrentGlossariesView(APIView, MyPaginationMixin):
    # получение списка справочников актуальных на указанную дату.
    queryset = None
    serializer_class = VersionsSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, date):

        if is_parameters_valid(date=date):
            self.queryset = get_current_versions(date)
            page = self.paginate_queryset(self.queryset)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response({"current glossaries": serializer.data})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ElementsGlossaryCurrentVersView(APIView, MyPaginationMixin):
    # получение элементов заданного справочника текущей версии
    queryset = None
    serializer_class = ElementsGlossarySerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, id):
        if is_parameters_valid(id=id):
            self.queryset = get_elements_current_glossary(id)
            page = self.paginate_queryset(self.queryset)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response({"Elements Glossary Current Version": serializer.data})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ElementsGlossarySpecVersView(APIView, MyPaginationMixin):
    # получение элементов заданного справочника указанной версии
    queryset = None
    serializer_class = ElementsGlossarySerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, id, version):
        if is_parameters_valid(id=id, slug=version):
            self.queryset = get_elements_glossary_cpec_ver(id, version)
            page = self.paginate_queryset(self.queryset)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response({"elements glossary specified version": serializer.data})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
