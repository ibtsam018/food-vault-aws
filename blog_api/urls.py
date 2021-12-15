from django.urls import path
from .views import PostList, PostDetail, PostUserList
from django.views.decorators.csrf import csrf_exempt

app_name = 'blog'

urlpatterns = [

    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('listing/<int:id>/', PostUserList.as_view(), name='userlisting'),

    path('', PostList.as_view(), name='listcreate'),


]
