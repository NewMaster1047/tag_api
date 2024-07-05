from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Tag
from .serializer import TagSerializer
from .utils import tag_creater


class TagListViewSet(ViewSet):

    def taglist(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class TagCreateViewSet(ViewSet):

    def tagcreate(self, request, *args, **kwargs):
        data = request.data.get('d')
        d = tag_creater(data)

        return Response({"result": d})
