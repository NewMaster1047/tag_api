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
        filter_get = kwargs.get('tag_name')
        filter_lower = filter_get.lower()
        filter = f"#{filter_lower}"

        tag_create(filter)

        filtered_posts = []

        url = "http://134.122.76.27:8111/api/v1/posts/"
        posts = dict(requests.get(url).json())
        post = posts.get('results')
        for i in post:
            d = i['description']
            filter_d = tag_filter(d)
            for f in filter_d:
                if f.lower() == filter:
                    filtered_posts.append(i)

        return Response(filtered_posts)
