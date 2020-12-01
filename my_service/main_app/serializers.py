from rest_framework import serializers

class GlossarySerializer(serializers.Serializer):
    name = serializers.CharField()
    short_name = serializers.CharField()
    description = serializers.CharField()