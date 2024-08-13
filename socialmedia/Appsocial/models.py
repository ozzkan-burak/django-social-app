from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="Post-Image")
  description = models.TesxtField()
  date = models.DateTimeField(auto_now_add=True)
  
class Commment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
