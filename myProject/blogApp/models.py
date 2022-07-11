from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 128, unique = True)
    content = models.CharField(max_length=2096)
    createdDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blogApp:post-detail', kwargs={'post_pk':self.pk})

class Comment(models.Model):
    text = models.CharField(max_length = 512)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('blogApp:post-detail', kwargs={'post_pk':self.post.pk})