# Generated by Django 3.2 on 2022-12-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
