from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 5

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    


class PostUserList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    print(Post.objects.all())
    serializer_class = PostSerializer
    
    def get_queryset(self):
        user = self.request.user

        print(user.id)
        return Post.objects.filter(author=user.id)

class FoodOnlyList(generics.ListAPIView):
    queryset = Post.objects.all()
    print(Post.objects.all())
    serializer_class = PostSerializer
    
    def get_queryset(self):
       
        return Post.objects.filter(itemcategory='food')

class NonFoodOnlyList(generics.ListAPIView):
    queryset = Post.objects.all()
    print(Post.objects.all())
    serializer_class = PostSerializer
    
    def get_queryset(self):
       
        return Post.objects.filter(itemcategory='nonfood')
