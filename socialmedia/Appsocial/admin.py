from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Commment)
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Follower)

# Register your models here.
