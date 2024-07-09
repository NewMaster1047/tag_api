from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from .models import Tag
from .serializer import TagSerializer, TagCreateSerializer, TagFilterSerializer
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


# class TagCreateViewSet(ViewSet):
#
#     @swagger_auto_schema(
#         operation_description="tag",
#         operation_summary="Create a new tag",
#         responses={200: TagSerializer()},
#         request_body=TagCreateSerializer(),
#         tags=['tag']
#     )
#     def tagcreate(self, request, *args, **kwargs):
#         data = request.data.get('d')
#         f_tag = tag_filter(data)
#         d = tag_create(f_tag)
#
#         return Response({"result": d})


class TagFilterViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="tag",
        operation_summary="Tag filter",
        responses={200: TagSerializer()},
        tags=['tag']
    )
    def tagfilter(self, request, *args, **kwargs):
        filter = kwargs.get('tag_name')
        filter = f"#{filter}"

        tag_create(filter)

        filtered_posts = []

        url = "http://134.122.76.27:8111/api/v1/posts/"
        posts = dict(requests.get(url).json())
        post = posts.get('results')
        for i in post:
            d = i['description']
            filter_d = tag_filter(d)
            for f in filter_d:
                if f == filter:
                    filtered_posts.append(i)

        return Response(filtered_posts)
