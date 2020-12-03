from rest_framework import serializers


class GlossarySerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    short_name = serializers.CharField()
    description = serializers.CharField()
    version = serializers.StringRelatedField(many=True)


class VersionsSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    glossary = serializers.StringRelatedField()
    version = serializers.CharField()
    initial_date = serializers.CharField()


class ElementsGlossarySerializer(serializers.Serializer):

    id = serializers.IntegerField()
    article = serializers.CharField()
    value = serializers.CharField()
