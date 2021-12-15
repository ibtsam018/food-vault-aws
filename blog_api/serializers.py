
from rest_framework import serializers
from blog.models import Post
from rest_flex_fields import FlexFieldsModelSerializer


class PostSerializer(FlexFieldsModelSerializer):
    author_name = serializers.CharField(
        source='author.username', read_only=True)
    author_ranger = serializers.CharField(
        source='author.is_ranger', read_only=True)
    author_image = serializers.CharField(
        source='author.image', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author_name', 'author_ranger', 'author_image', 'itemcategory', 'image', 'allergy', 'author', 'published', 'modified_on',
                  'excerpt', 'content', 'status')
