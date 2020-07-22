from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profile",on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    display_pic = models.ImageField(upload_to='pictures/', max_length=100)


class UserFollowing(models.Model):

    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ("user_id", "following_user_id")
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"


class Posts(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures/', max_length=100)
    caption = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    
