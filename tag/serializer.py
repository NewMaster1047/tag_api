from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )


class TagCreateSerializer(Serializer):
    d = serializers.CharField()

