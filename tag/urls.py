from django.urls import path
from .views import TagListViewSet, TagFilterViewSet

urlpatterns = [
    path('', TagListViewSet.as_view({'get': 'taglist'})),
    path('filter/<str:tag_name>/', TagFilterViewSet.as_view({'post': 'tagfilter'})),
]

