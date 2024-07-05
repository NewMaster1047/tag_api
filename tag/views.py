from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from .models import Tag
from .serializer import TagSerializer, TagCreateSerializer
from .utils import tag_creater


class TagListViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="info",
        operation_summary="Get all tags",
        responses={200: TagSerializer()},
    )
    def taglist(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class TagCreateViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="tag",
        operation_summary="Create a new tag",
        responses={200: TagSerializer()},
        request_body=TagCreateSerializer(),
        tags=['tag']
    )
    def tagcreate(self, request, *args, **kwargs):
        data = request.data.get('d')
        d = tag_creater(data)

        return Response({"result": d})
