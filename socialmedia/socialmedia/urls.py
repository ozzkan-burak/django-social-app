
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Appsocial.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
