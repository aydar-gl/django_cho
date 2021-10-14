from django.db import models

class Category(models.Model):
    name = models.CharField('Вид блюда', max_length=100, unique=True)
    slug = models.SlugField('URL', max_length=150, unique=True)
    image = models.ImageField('Изображение', upload_to=f'category/images/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Вид блюда'
        verbose_name_plural = 'Виды блюд'

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField('Наименование блюда', max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    slug = models.SlugField('URL', max_length=150, unique=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    grammers = models.IntegerField('Граммовки',default=0)
    image = models.ImageField('Изображение', upload_to=f'dish/images/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name

class Station(models.Model):
    address = models.CharField('Пункт', max_length=200, unique=True)

    class Meta:
        ordering = ('address',)
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'

    def __str__(self):
        return self.address

class Order(models.Model):
    client_name = models.CharField('ФИО клиента', max_length=200)
    client_number = models.CharField('Телефон клиента', max_length=50)
    client_mail = models.EmailField('Электронная почта клиента', max_length=254)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    dishes = models.ManyToManyField(Dish)
    order_price = models.DecimalField('Стоимость заказа', max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField('Статус заказа', default=False)

    class Meta:
        ordering = ('date',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.station} - {self.date}'