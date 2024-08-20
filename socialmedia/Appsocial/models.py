from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="Post-Image")
  description = models.TextField()
  likes = models.ManyToManyField(User, related_name="Likeds")
  post_saves = models.ManyToManyField(User, related_name="Saveds")
  date = models.DateTimeField(auto_now_add=True)
  
class Commment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="Profile-Image")
  bio = models.TextField()

class Follow(models.Model):
  profile = models.ForeignKey(Profile, related_name="follower_profile", on_delete=models.CASCADE)
  followed = models.ForeignKey(Profile, related_name="followed", on_delete=models.CASCADE)
  
class Follower(models.Model):
  profile = models.ForeignKey(Profile, related_name="follow_profile", on_delete=models.CASCADE)
  following = models.ForeignKey(Profile, related_name="following", on_delete=models.CASCADE)