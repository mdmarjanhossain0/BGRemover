from rest_framework import serializers
from image.models import Image

import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

IMAGE_SIZE_MAX_BYTES = 1024 * 1024 * 2  # 2MB
MIN_TITLE_LENGTH = 5
MIN_BODY_LENGTH = 50


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image", "width", "height"]

        # def save(self):
        #     try:

    # 		image = self.validated_data['image']

    #     except:
    #         print("exception")s
