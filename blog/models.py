from gettext import Catalog
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category',null=True,blank=True)
    image = models.ImageField(upload_to ='media')
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    content = models.TextField()
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    crated_at = models.DateTimeField(auto_now_add=True)

