from django.db import models
from account.models import Account
from django.conf import settings


class Like(models.Model):
    like_post = models.ForeignKey('ForumPost',on_delete=models.CASCADE)
    like_author=models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    comment_content = models.CharField(max_length=500)
    comment_post = models.ForeignKey('ForumPost',on_delete=models.CASCADE)
    comment_author=models.ForeignKey(Account,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

class ForumPost(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )

    post_text = models.CharField(max_length=1000)
    postcategory = models.CharField(max_length=500, null=True)
    published = models.DateField(auto_now_add=True, editable=False)
    publishedtime = models.TimeField(auto_now_add=True, editable=False)
    image = models.ImageField(upload_to='media', null=True)
    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='forum_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()
    postobjects = PostObjects()


    
    def get_like_post(self):
        return Like.objects.filter(like_post=self.id).values()

    def get_likes(self):
        
        return Like.objects.filter(like_post=self.id).count()
    
    def get_comments(self):
        
        return Comments.objects.filter(comment_post=self.id).count()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return str(self.id)

