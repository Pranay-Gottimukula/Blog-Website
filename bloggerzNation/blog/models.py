from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Defining a model for posts
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # Displaying posts in the order of posted time
    class Meta:
        ordering = ('-date_created',)

    # Returning name of the instance as title of post
    def __str__(self):
        return self.title
