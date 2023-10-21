from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    tag = TagsSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ('title', 'image', 'user', 'tag', 'description', 'user')


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image')


class TagSerializer(serializers.ModelSerializer):
    posts = PostsSerializer(many=True)

    class Meta:
        model = Tag
        fields = ('name', 'posts')


class CreatePostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Post
        fields = ('title', 'image', 'user', 'tag', 'description')