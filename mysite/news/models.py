from django.db import models

# Create your models here.
class Artiсles(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    anons = models.CharField(max_length=250,verbose_name='Анонс')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'