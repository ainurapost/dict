from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Category(models.Model):
    class ShoesType(models.TextChoices):
        Woman = 'Ж', _('Женский')
        Man = 'М', _('Мужской')

    shoes_type = models.CharField(
        max_length=1,
        choices=ShoesType.choices,
        default=ShoesType.Woman,
            )

    def __str__(self):
        return self.shoes_type

    class ShoesType2(models.TextChoices):
        Adult = 'Взр', _('Взрослый')
        Teen = 'Под', _('Подростковый')
        Child = 'Дет', _('Детский')

    shoes_type2 = models.CharField(
        max_length=3,
        choices=ShoesType2.choices,
        default=ShoesType2.Adult,
            )

    def is_adult(self):
        return self.shoes_type2 in {
            self.ShoesType2.Adult,
        }

    class Material(models.TextChoices):
        PU = 'PU', _('Polyurethane')
        EVA = 'EVA', _('EVA')

    material = models.CharField(
        max_length=3,
        choices=Material.choices,
        default=Material.PU,
    )

    def is_pu(self):
        return self.material in {
            self.Material.PU,
        }


class Year(models.Model):
    year = models.CharField(max_length=4, blank=True, verbose_name='Год выпуска')

    def __str__(self):
        return self.year


class Color(models.Model):
    color = models.CharField(max_length=100, blank=True, verbose_name='Цвет')

    def __str__(self):
        return self.color


class Product(models.Model):
    model_code = models.CharField(max_length=100, verbose_name='Код модели', db_index=True)
    type = models.CharField(max_length=100, verbose_name='Тип', blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='Описание', null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фото', blank=True, null=True)
    is_available = models.BooleanField(default=True, verbose_name='в наличии', null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name='Цвет')
    year = models.ForeignKey('Year', on_delete=models.CASCADE, verbose_name='Год выпуска')

    def __str__(self):
        return f'{self.pk} - {self.model_code}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['year']


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование клиента', db_index=True)
    info = models.CharField(max_length=500, verbose_name='Информаци о клиенте', blank=True, null=True)
    is_debtor = models.BooleanField(default=True, verbose_name='имеет задолженность', null=True)
    client_debt = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_client', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name']


class Order(models. Model):
    model_code = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Модель товара')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Наименование клиента', db_index=True)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    debt = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    def __str__(self):
        return f'{self.client} - {self.debt}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

