from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

class Genre(TimeStampedModel):
    name = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)

    class Meta:
        verbose_name = _('жанр')
        verbose_name_plural = _('жанры')

    def __str__(self):
        return self.name


class FilmworkType(models.TextChoices):
    MOVIE = 'movie', _('фильм')
    TV_SHOW = 'tv_show', _('шоу')


class ProfessionType(models.TextChoices):
    DIRECTOR = 'director', _('режиссер')
    ACTOR = 'actor', _('актер')
    WRITER = 'writer', _('сценарист')


class Filmwork(TimeStampedModel):

    type = models.CharField(_('тип'), max_length=20, choices=FilmworkType.choices)
    title = models.CharField(_('заголовок'), max_length=255)
    description = models.TextField(_('содержание'), blank=True)
    creation_date = models.DateField(_('дата создания'), blank=True)
    age_rating = models.TextField(_('возрастной ценз'), blank=True)
    genres = models.ManyToManyField(Genre)
    link = models.URLField(_('ссылка на файл'), blank=True)
    class Meta:
        verbose_name = _('кинопроизведение')
        verbose_name_plural = _('кинопроизведения')

    def __str__(self):
        return self.title


class Person(TimeStampedModel):
    type = models.CharField(_('тип'), max_length=20, choices=ProfessionType.choices)
    name = models.CharField(_('имя'), max_length=255)
    last_name = models.CharField(_('фамилия'), max_length=255)
    film = models.ForeignKey(Filmwork, on_delete=models.CASCADE, blank=True)
    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self):
        return f'{self.name} {self.last_name}'

















