from django.contrib.auth.models import AbstractUser
from django.db import models


class SnakeUser(AbstractUser):
    easy_hightscore = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Easy mode hightscore',
    )
    easy_avg_score = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Easy mode average score',
    )
    medium_hightscore = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Medium mode hightscore',
    )
    medium_avg_score = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Medium mode average score',
    )
    hard_hightscore = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Hard mode hightscore',
    )
    hard_avg_score = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Hard mode average score',
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
