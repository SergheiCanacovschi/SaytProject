# Generated by Django 4.0.5 on 2022-09-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_images_novosti_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='model_img',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
