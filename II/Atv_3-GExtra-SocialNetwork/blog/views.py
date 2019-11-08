from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from .models import *
import json


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-list'


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class CommentDetail(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'


class ProfilePostList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-list'


class ProfilePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-detail'


class PostCommentsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer
    name = 'post-comments-list'


class PostCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer
    name = 'post-comments-detail'


class PostCommentsUpdateList(APIView):
    name = 'post-comments-update-list'

    def get(self, request, pk_post, pk_comment):
        try:
            post = Post.objects.get(pk=pk_post)
            comment = post.comments.get(pk=pk_comment)
        except Exception:
            return Response(status.HTTP_404_NOT_FOUND)

        comment_serializer = PostCommentsUpdateSerializer(comment)
        return Response(comment_serializer.data)

    def put(self, request, pk_post, pk_comment):
        try:
            post = Post.objects.get(pk=pk_post)
            comment = post.comments.get(pk=pk_comment)
        except Exception:
            return Response(status.HTTP_404_NOT_FOUND)

        comment_serializer = PostCommentsUpdateSerializer(comment, data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data)
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_post, pk_comment):
        try:
            post = Post.objects.get(pk=pk_post)
            comment = post.comments.get(pk=pk_comment)
        except Exception:
            try:
                post = Post.objects.get(pk=pk_post)
                comment = post.comments.get(pk=pk_comment)
            except Exception:
                return Response(status.HTTP_404_NOT_FOUND)

            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileReport(APIView):
    name = 'profile-report-list'

    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        posts = profile.posts.all()
        comments = []
        for post in posts:
            comments.extend(post.comments.all())

        return Response({
            'pk': pk,
            'name': profile.name,
            'total_posts': len(posts),
            'total_comments': len(comments)
        }, status=status.HTTP_200_OK)


class ProfilePostsComments(APIView):
    name = 'profile-posts-comments'

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        status_list = []

        for profile in profiles:
            profile_status = {}
            profile_posts = 0
            post_comments = 0

            for post in Post.objects.filter(userId=profile.pk):
                profile_posts += 1
                for comment in Comment.objects.filter(postId=post.pk):
                    post_comments += 1

            profile_status['pk'] = profile.pk
            profile_status['name'] = profile.name
            profile_status['total_posts'] = profile_posts
            profile_status['total_comments'] = post_comments

            status_list.append(profile_status)

        return Response(status_list, status=status.HTTP_200_OK)


class ImportData(generics.GenericAPIView):
    name = 'import_data'

    def get(self, request, *args, **kwargs):
        self.import_data()
        return redirect(ApiRoot.name)

    def import_data(self):
        file = open('db.json')
        object = ''

        for line in file:
            object += line.strip()
        dict_json = json.loads(object)

        for user in dict_json['users']:
            pre_address = user['address']
            address = Address(street=pre_address['street'], suite=pre_address['suite'], city=pre_address['city'],
                              zipcode=pre_address['zipcode'])
            address.save()
            Profile.objects.create(name=user['name'], email=user['email'], address=address)

        for post in dict_json['posts']:
            user = Profile.objects.get(id=post['userId'])
            Post.objects.create(title=post['title'], body=post['body'], userId=user)

        for comment in dict_json['comments']:
            post = Post.objects.get(id=comment['postId'])
            Comment.objects.create(name=comment['name'], email=comment['email'], body=comment['body'], postId=post)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profile': reverse(ProfileList.name, request=request),
            'profile-posts': reverse(ProfilePostList.name, request=request),
            'posts-comments-all': reverse(PostCommentsList.name, request=request),
            # 'profile-posts-comments': reverse(ProfilePostsComments.name, request=request),
        })
