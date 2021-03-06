# Generated by Django 4.0 on 2021-12-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('lname', models.CharField(blank=True, max_length=30, null=True)),
                ('fname', models.CharField(blank=True, max_length=30, null=True)),
                ('mname', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 'delivery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('flower_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Фотография букета')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'db_table': 'flower',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FlowerList',
            fields=[
                ('flower_list_id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'flower_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('order_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('color', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'db_table': 'order_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('payment_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'payment_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('is_admin', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'position',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=32, null=True)),
                ('session', models.CharField(blank=True, max_length=32, null=True)),
                ('lname', models.CharField(blank=True, max_length=30, null=True)),
                ('fname', models.CharField(blank=True, max_length=30, null=True)),
                ('mname', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
    ]
