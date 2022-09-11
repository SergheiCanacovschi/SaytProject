from django.db import models
from django import forms
from django.urls import reverse


class Novosti(models.Model):
     data = models.DateField(max_length=30,
                            help_text="Введите дату публицакий ",
                            verbose_name="Дата публикация")
     vremea = models.TimeField(max_length=30,
                            help_text="Введите время публицакий ",
                            verbose_name="Время публикация")
     persona = models.CharField(max_length=60,
                            help_text="Введите атвора публикаций ",
                            verbose_name="Автор Публикаций")
     title = models.CharField(max_length=75,
                              help_text="Введите заголовок Новостей",
                              verbose_name="Заголовок Новостей")
     summary = models.TextField(max_length=10000,
                                help_text="Описание Новостей", 
                                verbose_name="Описание ")
     file = models.FileField(null=True, blank=True,
                               verbose_name="Вы можете прикрепить файл")
     image = models.ImageField(null=True, blank=True,upload_to='image/',
                               verbose_name="Вы можете прикрепить фото") 

     def __str__(self):
         return self.title



class Rasporejenia(models.Model):
    data = models.DateField(max_length=30,
                            help_text="Введите дату публицакий ",
                            verbose_name="Дата публикация")
    vremea = models.TimeField(max_length=30,
                            help_text="Введите время публицакий ",
                            verbose_name="Время публикация")
    last_name = models.CharField(max_length=50,
                            help_text="Введите атвора публикаций",
                            verbose_name="Автор Публикаций")
    title = models.CharField(max_length=150,
                             help_text="Введите заголовок Документа",
                             verbose_name="Заголовок Документа")
    summary = models.TextField(max_length=10000,
                               help_text="Описание Документа", verbose_name="Описание ")
    file = models.FileField(null=True, blank=True, upload_to='image',
                               verbose_name="Вы можете прикрепить файл")    
    image = models.ImageField(null=True, blank=True, upload_to='static/image',
                               verbose_name="Вы можете прикрепить фото")

class KCS(models.Model):
    data = models.DateField(max_length=30,
                            help_text="Введите дату публицакий ",
                            verbose_name="Дата публикация")
    vremea = models.TimeField(max_length=30,
                            help_text="Введите время публицакий ",
                            verbose_name="Время публикация")
    last_name = models.CharField(max_length=50,
                            help_text="Введите атвора публикаций",
                            verbose_name="Автор Публикаций")
    title = models.CharField(max_length=150,
                             help_text="Введите заголовок Документа",
                             verbose_name="Заголовок Документа")
    summary = models.TextField(max_length=10000,
                               help_text="Описание Документа", verbose_name="Описание ")
    file = models.FileField(null=True, blank=True, upload_to='image',
                               verbose_name="Вы можете прикрепить файл")    
    image = models.ImageField(null=True, blank=True, upload_to='static/image',
                               verbose_name="Вы можете прикрепить фото")

    def __str__(self):
        return '%s %s' % (self.data, self.title)

