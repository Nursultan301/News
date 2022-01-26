from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Rubric(MPTTModel):
    name = models.CharField('Название', max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Родитель')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rubric', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Рубрик'
        verbose_name_plural = 'Рубрики'

    class MPTTMeta:
        order_insertion_by = ['name']


class Article(models.Model):
    name = models.CharField('Название', max_length=50)
    category = TreeForeignKey(Rubric, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
