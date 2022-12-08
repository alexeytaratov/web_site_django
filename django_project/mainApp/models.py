from django.db import models

# Create your models here.
class Task(models.Model): # создаём класс с задачами
    title = models.CharField('Название', max_length=255)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta: # короче это нужно, чтобы в админ-панели Django таблица называлась не так,
                # как мы назвали класс (Tasks), а так, как мы сами захотим.
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
