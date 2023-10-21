from rest_framework.viewsets import ModelViewSet

from .models import Post, Tag
from .serializers import PostSerializer, PostsSerializer, CreatePostSerializer, TagSerializer, TagsSerializer
from .permissions import PostAuthenticatedUpdateOwner


class PostView(ModelViewSet):
    permission_classes = [
        PostAuthenticatedUpdateOwner
    ]

    def get_queryset(self):
        if self.action == 'retrieve':
            return Post.objects.all().select_related(
                'user', 
            ).prefetch_related(
                'tag',
            ).only(
                'title',
                'image',
                'description',
                'user__id',
                'user__username',
                'tag__name',
                'tag__id'
            )

        return Post.objects.all().only(
                'id',
                'image',
                'created_at',
            )


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostSerializer
        if self.action == 'create':
            return CreatePostSerializer
        if self.action == 'update':
            return CreatePostSerializer
        return PostsSerializer


class TagView(ModelViewSet):
    def get_queryset(self):
        if self.action == 'retrieve':
            return Tag.objects.all()
        return Tag.objects.all()


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TagSerializer
        return TagsSerializer