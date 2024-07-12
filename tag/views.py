from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Tag
from .serializer import TagSerializer
from .utils import tag_create, tag_filter
import requests
from django.conf import settings


class TagListViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="info",
        operation_summary="Get all tags",
        responses={200: TagSerializer()},
    )
    def taglist(self, request, *args, **kwargs):
        gettoken_url = f"{settings.URL_TOKEN_SERVICE}/login/"
        get_token = requests.post(gettoken_url,
                                  data={
                                      "service_id": 5,
                                      "service_name": "Tag",
                                      "secret_key": "ba27a5a2-cec3-45d7-ab8e-eba0a16d3bc9"
                                  }).json()
        getpost_url = f"{settings.URL_POST_SERVICE}/posts/list/"
        posts = requests.post(getpost_url, data={"token": get_token['token']}).json()

        for i in posts:
            description = i['description']
            if description is not None:
                tag_filter(description, '')

        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)

        val = []

        for i in serializer.data:
            dict_values = i['name']
            val.append(dict_values)

        return Response(val, status=status.HTTP_200_OK)


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

        gettoken_url = f"{settings.URL_TOKEN_SERVICE}/login/"
        get_token = requests.post(gettoken_url,
                                  data={
                                      "service_id": 5,
                                      "service_name": "Tag",
                                      "secret_key": "ba27a5a2-cec3-45d7-ab8e-eba0a16d3bc9"
                                  }).json()
        filtered_posts = []

        getpost_url = f"{settings.URL_POST_SERVICE}/posts/list/"
        posts = requests.post(getpost_url, data={"token": get_token['token']}).json()

        for i in posts:
            description = i['description']
            if description is not None:
                tag_f = tag_filter(description, tag)
                if tag_f is True:
                    filtered_posts.append(i)
                    tag_create(tag)

        return Response(filtered_posts, status=status.HTTP_200_OK)
