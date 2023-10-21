from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'posts/user_{0}/{1}'.format(instance.user.id, filename)


class Post(models.Model):
    title       = models.CharField(
                                max_length=135,
                                verbose_name='Заголовок'
    )
    image       = models.ImageField(
                                upload_to=user_directory_path,
                                verbose_name='Изображение'
    )
    user        = models.ForeignKey(
                                User,
                                on_delete=models.CASCADE,
                                related_name='users',
                                verbose_name='Пользователь'
    )
    tag         = models.ManyToManyField(
                                'Tag',
                                db_index=True,
                                related_name='posts',
                                verbose_name='Тег(и)'
    )
    created_at  = models.DateTimeField(
                                auto_now_add=True,
                                verbose_name='Дата публикации'
    )
    description = models.TextField(
                                max_length=500,
                                verbose_name='Описание',
                                blank=True
    )

    class Meta:
        ordering = ('created_at',)


    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тег(и)')

    class Meta:
        ordering = ('name',)


    def __str__(self) -> str:
        return self.name
