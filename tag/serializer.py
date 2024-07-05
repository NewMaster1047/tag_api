from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )

