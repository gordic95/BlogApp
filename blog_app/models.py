from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='Номер телефона')
    bio = models.TextField(blank=True, verbose_name='Биография')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ,
        related_name="custom_user_groups",  # Новое имя обратного отношения
        related_query_name="custom_group",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",  # Новое имя обратного отношения
        related_query_name="custom_permission",
    )

    def __str__(self):
        return self.username



class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tags(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Тег')
    posts = models.ForeignKey('Post', on_delete=models.PROTECT, null=True, verbose_name='Посты', blank=True)
    cats = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

