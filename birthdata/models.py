from django.db import models


class Town(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='название города'
    )

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'

    def __str__(self):
        return self.name


class Writer(models.Model):
    firstname = models.CharField(max_length=100, verbose_name='имя')
    lastname = models.CharField(max_length=100, verbose_name='фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='отчество')
    birth_place = models.ForeignKey(
        to=Town,
        on_delete=models.SET_NULL,
        null=True,
        related_name='writers',
        verbose_name='место рождения'
    )
    birth_date = models.DateField(verbose_name='дата рождения')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['firstname', 'lastname', 'patronymic'],
                name='unique_writer'
            )
        ]
        verbose_name_plural = 'Писатели'
        verbose_name = 'Писатель'

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.firstname} {self.patronymic} {self.lastname}'
