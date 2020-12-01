from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from main_app.models import Glossary
from .serializers import GlossarySerializer




class GlossaryView(APIView):

    def get(self, request):
        articles = Glossary.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = GlossarySerializer(articles, many=True)
        return Response({"glossaries": serializer.data})