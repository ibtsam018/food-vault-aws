from django.shortcuts import render
from rest_framework import generics
from .models import ForumPost, Like, Comments
from .serializers import ForumSerializer, PostlikeSerializer, PostCommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ForumList(generics.ListCreateAPIView):
    queryset = ForumPost.postobjects.all()
    serializer_class = ForumSerializer

class ForumUpdateList(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.postobjects.all()
    serializer_class = ForumSerializer

class LikeListCreate(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = PostlikeSerializer

class LikeDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = PostlikeSerializer

    def delete(self, request, pk):
        user = self.request.user

        Like.objects.filter(like_author=user.id, like_post=pk).delete()
        return Response ({
            'status': 'ok'
        })

class LikeView(APIView):
    queryset = Like.objects.all()
    serializer_class = PostlikeSerializer

    def get(self, request, postid):
        user = self.request.user

        print(postid)
        likes=Like.objects.filter(like_author=user.id, like_post=postid).values()
        if likes:
            likes=True
        else:
            likes = False    
        return Response ({
            'likes': likes
        })

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = PostCommentSerializer

class PostComment(APIView):
    queryset = Comments.objects.all()
    serializer_class = PostCommentSerializer

    def get(self, request, postid):

        comments=Comments.objects.filter(comment_post=postid)
        serializer = PostCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = self.request.user

        Comments.objects.filter( id=pk).delete()
        return Response ({
            'status': 'ok'
        })    