from django.db import models
from account.models import Account
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    allergy = models.TextField(null=True)
    itemcategory = models.CharField(max_length=500, null=True)
    published = models.DateField(auto_now_add=True, editable=False)
    phone = models.CharField(max_length=100,null=True, blank=True, unique=False, default=None)
    modified_on = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media', default='default.jpg')
    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    country_user = models.CharField(max_length=100, default='Pakistan', null=True)
    is_requested_item = models.BooleanField(default=False)
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
