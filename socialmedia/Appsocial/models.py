from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="Post-Image")
  description = models.TesxtField()
  likes = models.ManyToManyField(User)
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
  profile = models.ForeignKey(Profile, releated_name="profile" on_delete=models.CASCADE)
  followed = models.ForeignKey(Profile, releated_name="followed" on_delete=models.CASCADE)
  
class Follower(models.Model):
  profile = models.ForeignKey(Profile, releated_name="profile" on_delete=models.CASCADE)
  following = models.ForeignKey(Profile, releated_name="following" on_delete=models.CASCADE)