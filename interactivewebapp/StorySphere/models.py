from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class ForumTopic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ForumComment(models.Model):
    topic = models.ForeignKey(ForumTopic, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(ForumTopic, related_name='likes', on_delete=models.CASCADE)
    comment = models.ForeignKey(ForumComment, related_name='likes', on_delete=models.CASCADE, null=True, blank=True)