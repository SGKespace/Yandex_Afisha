from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название места', max_length=100, unique=True,)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField("Подробное описание", blank=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='')
    place = models.ForeignKey(
        'Place', verbose_name='Место', related_name='images', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('Позиция', default=0, db_index=True, blank=True)


    class Meta(object):
        ordering = ('position',)


    def __str__(self):
        return f'{self.id} {self.place.title}'


    @property
    def get_preview(self):
        if self.image:
            return format_html(
                mark_safe('<img src="{}" style="max-height:300px, max-height: 300px">'),
                self.image.url,
                )
        return ""
