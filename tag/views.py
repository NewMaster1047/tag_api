from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from .models import Tag
from .serializer import TagSerializer
from .utils import tag_create, tag_filter
import requests


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


class TagFilterViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="tag",
        operation_summary="Tag filter",
        responses={200: TagSerializer()},
        tags=['tag']
    )
    def tagfilter(self, request, *args, **kwargs):
        get_tag = kwargs.get('tag_name')
        tag_lowered = get_tag.lower()
        tag = f"#{tag_lowered}"

        filtered_posts = []

        url = "http://134.122.76.27:8111/api/v1/posts/"
        posts = requests.get(url).json()
        post = posts.get('results')
        for i in post:
            description = i['description']
            tag_f = tag_filter(description, tag)
            if tag_f is True:
                filtered_posts.append(i)

        return Response(filtered_posts)

