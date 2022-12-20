from django.urls import path
from image.api.views import api_upload_image

app_name = "image"

urlpatterns = [
    path("upload", api_upload_image, name="upload"),
]
