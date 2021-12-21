# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    lname = models.CharField(max_length=30, blank=True, null=True, verbose_name='Фамилия клиента')
    fname = models.CharField(max_length=30, blank=True, null=True, verbose_name='Имя клиента')
    mname = models.CharField(max_length=30, blank=True, null=True, verbose_name='Отчество клиента')
    phone = models.CharField(max_length=13, blank=True, null=True, verbose_name='Телефон клиента')

    def __str__(self):
        return f"{self.client_id}|{self.lname} | {self.fname} | {self.mname} | {self.phone}"

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True, verbose_name='Дата доставки')
    address = models.CharField(max_length=70, blank=True, null=True, verbose_name='Адрес доставки')

    def __str__(self):
        return self.delivery_id

    class Meta:
        managed = False
        db_table = 'delivery'
        verbose_name = 'Доставку'
        verbose_name_plural = 'Доставка'


class Flower(models.Model):
    flower_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, blank=True, null=True, verbose_name='Название букета')
    photo = models.ImageField(upload_to='images/', verbose_name='Фотография букета')
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, verbose_name='Стоимость букета')
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True, verbose_name='Категория букета')

    def __str__(self):
        return f"{self.flower_id} | {self.name} | {self.price} | {self.category}"

    class Meta:
        managed = False
        db_table = 'flower'
        app_label = 'main'
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'


class FlowerList(models.Model):
    flower_list_id = models.AutoField(primary_key=True)
    count = models.IntegerField(blank=True, null=True, verbose_name='Количество')
    orders = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True, verbose_name='Заказ')
    flower = models.ForeignKey(Flower, models.DO_NOTHING, blank=True, null=True, verbose_name='Букет')

    def __str__(self):
        return self.flower_list_id

    class Meta:
        managed = False
        db_table = 'flower_list'
        verbose_name = 'Список букетов'
        verbose_name_plural = 'Списки букетов'


class OrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Название статуса')
    color = models.CharField(max_length=6, blank=True, null=True, verbose_name='Цвет статуса заказа')

    def __str__(self):
        return f"{self.name} | {self.color}"

    class Meta:
        managed = False
        db_table = 'order_status'
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статус заказа'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, verbose_name='Стоимость заказа')
    staff = models.ForeignKey('Staff', models.DO_NOTHING, blank=True, null=True, verbose_name='Сотрудник')
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True, verbose_name='Клиент')
    order_status = models.ForeignKey(OrderStatus, models.DO_NOTHING, blank=True, null=True, verbose_name='Статус заказа')
    delivery = models.ForeignKey(Delivery, models.DO_NOTHING, blank=True, null=True, verbose_name='Доставка')
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING, blank=True, null=True, verbose_name='Тип оплаты')

    def __str__(self):
        return self.order_id

    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Название оплаты')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'payment_type'
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'


class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Название должности')
    is_admin = models.BooleanField(blank=True, null=True, verbose_name='Админ')

    def __str__(self):
        return f"{self.position_id} | {self.name}"

    class Meta:
        managed = False
        db_table = 'position'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=30, blank=True, null=True, verbose_name='Логин')
    password = models.CharField(max_length=32, blank=True, null=True, verbose_name='Пароль')
    session = models.CharField(max_length=32, blank=True, null=True, verbose_name='Сессия')
    lname = models.CharField(max_length=30, blank=True, null=True, verbose_name='Фамилия сотрудника')
    fname = models.CharField(max_length=30, blank=True, null=True, verbose_name='Имя сотрудника')
    mname = models.CharField(max_length=30, blank=True, null=True, verbose_name='Отчество сотрудника')
    phone = models.CharField(max_length=13, blank=True, null=True, verbose_name='Телефон сотрудника')
    position = models.ForeignKey(Position, models.DO_NOTHING, blank=True, null=True, verbose_name='Должность')

    def __str__(self):
        return f"{self.staff_id} | {self.login} | {self.lname} | {self.fname} | {self.mname} | {self.position}"

    class Meta:
        managed = False
        db_table = 'staff'
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'
