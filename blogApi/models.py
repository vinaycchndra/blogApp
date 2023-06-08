from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    portfolio_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=200)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    title_tag = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = RichTextField(blank=True, null = True)
    date_publication = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=1000)
    def __str__(self):
        return self.title+' | '+str(self.auther)

class Likes(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.auther.first_name+" liked "+ self.article.title


class CommentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(parent=None)


class Comments(models.Model):
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField();
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    nonParent = CommentsManager()
    objects = models.Manager()
    class Meta:
        ordering = ['date_added']


    def all_children(self):
        return Comments.objects.filter(parent=self)

    def __str__(self):
        return '%s - %s' % (self.article.title, self.commentator.first_name)

