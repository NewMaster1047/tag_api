from django.urls import path
from .views import TagListViewSet, TagCreateViewSet

urlpatterns = [
    path('', TagListViewSet.as_view({'get': 'taglist'})),
    path('create/', TagCreateViewSet.as_view({'post': 'tagcreate'})),
]

