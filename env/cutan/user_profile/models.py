from django.db import models
from django.contrib.auth.models import User


def user_directory(instance, filename):
    return 'profile/user_{0}/{1}'.format(instance.user.id, filename)


class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)


    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user        = models.OneToOneField(
                                User,
                                on_delete=models.CASCADE,
                                related_name='profiles',
                                verbose_name='Пользователь'
    )
    email       = models.EmailField(
                                verbose_name='Почта',
                                blank=True
    )
    description = models.TextField(
                                max_length=1000,
                                verbose_name='Описание'
    )
    created_at  = models.DateTimeField(
                                auto_now_add=True,
                                verbose_name='Дата регистрации'
    )
    сountry     = models.ForeignKey(
                                Country,
                                on_delete=models.SET_DEFAULT,
                                default='Unknown',
                                verbose_name='Страна'
    )
    avatar      = models.ImageField(
                                upload_to=user_directory,
                                verbose_name='Изображение',
                                blank=True
    )

    def __str__(self) -> str:
        return str(self.user)
