from rest_framework import serializers

from .models import ForumPost, Like, Comments
from rest_framework.exceptions import AuthenticationFailed

class PostlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class ForumSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(
        source='author.username', read_only=True)
    author_image = serializers.CharField(
        source='author.image', read_only=True)

    class Meta:
        model = ForumPost
        fields = ('id','post_text','postcategory','published','publishedtime','image','author', 'get_likes','author_name', 'get_like_post','get_comments','author_image')


class PostCommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source='comment_author.username', read_only=True)
    author_image = serializers.CharField(
        source='comment_author.image', read_only=True)
    class Meta:
        model = Comments
        fields = ('id', 'comment_content', 'comment_post', 'comment_author', 'author_username','author_image','created')