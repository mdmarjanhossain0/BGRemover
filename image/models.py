from django.db import models

from datetime import datetime


def upload_loacation(instance,filename):
	file_path = 'img/{time}-{filename}{extention}'.format(
			time = datetime.now(),
			filename = filename.split(".")[0],
			extention = ".png"
		)
	return file_path

class Image(models.Model):
    image=models.ImageField(upload_to = upload_loacation)