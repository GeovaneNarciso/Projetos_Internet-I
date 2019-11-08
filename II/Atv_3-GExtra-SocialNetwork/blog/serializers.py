from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ['pk', 'name', 'email', 'address']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # post = serializers.SlugRelatedField(Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'postId']


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'body', 'userId']


class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
    # address = serializers.SlugRelatedField(Address.objects.all(), slug_field='street')
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['pk', 'name', 'email', 'address', 'posts']


class PostCommentsSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'userId', 'comments']


class PostCommentsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'postId')
