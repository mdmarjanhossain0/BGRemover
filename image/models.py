from django.db import models


def upload_loacation(instance,filename):
	file_path = 'img/{filename}'.format(
			filename = filename
		)
	return file_path

class Image(models.Model):
    image=models.ImageField(upload_to = upload_loacation)