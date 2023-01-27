from django.db import models
from transliterate import slugify


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    description_1 = models.CharField(max_length=100, verbose_name='Описание 1')
    description_2 = models.CharField(max_length=100, verbose_name='Описание 2')
    description_3 = models.CharField(max_length=100, verbose_name='Описание 3')
    description_4 = models.CharField(max_length=100, verbose_name='Описание 4')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f' {self.name} {self.price} {self.description_1} {self.description_2} {self.description_3} {self.description_4}'


class Category(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.id} {self.name}'


class Blog(models.Model):
    STATUS_ACTIVE = 'True'
    STATUS_INACTIVE = 'False'
    STATUSES = (
        (STATUS_ACTIVE, 'положительный'),
        (STATUS_INACTIVE, 'отрицательный')
    )
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    heading = models.CharField(max_length=250, verbose_name='Заголовк')
    slug = models.CharField(max_length=250, unique=True, verbose_name='slug')
    content = models.CharField(max_length=250, verbose_name='Содержимое')
    image = models.FileField(upload_to="images/", verbose_name='Изображение', null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUSES, default=STATUS_ACTIVE, max_length=15)
    view = models.IntegerField(verbose_name='Просмотры', default=0)


    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.heading))
        super(Blog, self).save(*args, **kwargs)
