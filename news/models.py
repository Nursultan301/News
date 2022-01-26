from django.db import models
from django.urls import reverse


class Category(models.Model):
    """ Категория """
    title = models.CharField('Наименование катигории', max_length=150, db_index=True)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']


class News(models.Model):
    """ Новости """
    title = models.CharField(' Наименование ', max_length=150)
    content = models.TextField('Контент', blank=True)
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория',
                                 related_name='category')
    views = models.IntegerField('Просмотр', default=0)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("view_news", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
