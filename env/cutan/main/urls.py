from django.urls import path, include
from rest_framework import routers

from .views import PostView, TagView


router_post = routers.DefaultRouter()
router_post.register('', PostView, basename='post')

router_tag = routers.DefaultRouter()
router_tag.register('', TagView, basename='tag')

urlpatterns = [
    path('post/', include(router_post.urls)),
    path('tag/', include(router_tag.urls)),
]
