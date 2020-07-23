from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class User(AbstractUser):

    bio = models.TextField(max_length=500, blank=True)
    display_pic = models.ImageField(upload_to='pictures/', max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()
    


# @receiver(post_save, sender=User)       # called after User model gets saved
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



# class UserFollowing(models.Model):

#     user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE, null=True, blank=True)
#     following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE, null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True, db_index=True)

#     class Meta:
#         unique_together = ("user_id", "following_user_id")
#         ordering = ["-created"]

#     def __str__(self):
#         return f"{self.user_id} follows {self.following_user_id}"


class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures/', max_length=100)
    caption = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    
