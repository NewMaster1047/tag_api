from django.urls import path
from .views import TagListViewSet, TagCreateViewSet, TagFilterViewSet

urlpatterns = [
    path('', TagListViewSet.as_view({'get': 'taglist'})),
    path('create/', TagCreateViewSet.as_view({'post': 'tagcreate'})),
    path('filter/<str:tag_name>/', TagFilterViewSet.as_view({'post': 'tagfilter'})),

]

