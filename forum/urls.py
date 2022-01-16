from django.urls import path
from .views import ForumList, ForumUpdateList, LikeListCreate, LikeDelete, LikeView, CommentListCreate, PostComment

app_name = 'forum'

urlpatterns = [


    path('', ForumList.as_view(), name='forumlist'),
    path('info/<int:pk>', ForumUpdateList.as_view(), name='forumupdatelist'),
 
    path('<int:pk>/like/',LikeListCreate.as_view(),name = 'post_likes'),
    path('likeget/<int:postid>/',LikeView.as_view(),name = 'post_likes_get'),
    path('<int:pk>/delete-like/',LikeDelete.as_view(),name = 'delete_likes'),
    path('comments/',CommentListCreate.as_view(),name = 'comment-list'),
    path('comments/<int:postid>',PostComment.as_view(),name = 'comment-list'),
    path('comments/delete/<int:pk>',PostComment.as_view(),name = 'comment-delete'),
    

]
