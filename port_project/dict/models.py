from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import date


class Category(models.Model):
    MAN_WOMAN = (
        ('Ж', 'Женский'),
        ('М', 'Мужской'),
    )

    cat = models.CharField(max_length=2, choices=MAN_WOMAN, default='Ж')

    def __str__(self):
        return self.cat

    def get_absolute_url(self):
        return reverse('view_wm', kwargs={'id': self.pk})


class AGE(models.Model):
    AGE = (
        ('Взр', 'Взрослый'),
        ('Под', 'Подростковый'),
        ('Дет', 'Детский'),
    )

    age = models.CharField(max_length=6, choices=AGE, default='Взр')

    def __str__(self):
        return self.age


class Material(models.Model):
    PU_EVA = (
        ('PU', 'Polyurethane'),
        ('EVA', 'EVA'),
    )

    material = models.CharField(max_length=3, choices=PU_EVA, default='PU')

    def __str__(self):
        return self.material

    def get_absolute_url(self):
        return reverse('view_material', kwargs={'id': self.pk})


class Year(models.Model):
    year = models.CharField(max_length=4, blank=True, verbose_name='Год выпуска')

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Год выпуска'
        verbose_name_plural = 'Год выпуска'
        ordering = ['id']


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
    MW = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Муж_Жен')
    color = models.ForeignKey('Color', on_delete=models.CASCADE, verbose_name='Цвет')
    year = models.ForeignKey('Year', on_delete=models.CASCADE, verbose_name='Год выпуска')
    age = models.ForeignKey('AGE', on_delete=models.PROTECT, verbose_name='Возраст_тип')
    material = models.ForeignKey('Material', on_delete=models.PROTECT, verbose_name='Материал')
    delivered_date=models.DateField(default=date.today, blank=True)

    def __str__(self):
        return self.model_code

    def get_absolute_url(self):
        return reverse('view_product', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-delivered_date']


class Client(models.Model):
    client_name = models.CharField(max_length=200, verbose_name='Наименование клиента', db_index=True)
    info = models.CharField(max_length=500, verbose_name='Информация о клиенте', blank=True, null=True)
    is_debtor = models.BooleanField(default=True, verbose_name='имеет задолженность', null=True)
    client_debt = models.IntegerField(default=True)


    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('view_client', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['client_name']

    # @property
    # def client_orders(self):
    #     return self.client_orders.all()


class Order(models.Model):
    model_code = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Модель товара')
    client_name = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Наименование клиента')
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    debt = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    def __str__(self):
        return f'{self.model_code} - {self.client_name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['id']
