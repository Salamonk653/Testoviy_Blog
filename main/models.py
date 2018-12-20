from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    # класс категории
    title = models.CharField('Название', max_length=50)


    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.title

class Teg(models.Model):
    # класс категории
    title = models.CharField('Тег', max_length=50)

    class Meta():
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


# Create your models here.
class Posts(models.Model):
    # класс новостей
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    title = models.CharField('Заголовок', max_length=100)
    text_min = models.TextField('Мин текст', max_length=350)
    text = models.TextField('Текст статьи')
    tag = models.ManyToManyField(Teg, verbose_name='Теги')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    description = models.CharField('Описание', max_length=100)
    keywords = models.CharField('Ключевые слова', max_length=50)

    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title