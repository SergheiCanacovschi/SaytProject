# Generated by Django 4.1 on 2022-08-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0005_document_file_alter_novosti_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Вы можете прикрепить фото'),
        ),
    ]
