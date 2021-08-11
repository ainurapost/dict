# Generated by Django 3.2.6 on 2021-08-08 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0004_alter_year_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование клиента')),
                ('info', models.CharField(blank=True, max_length=500, null=True, verbose_name='Информаци о клиенте')),
                ('is_debtor', models.BooleanField(default=True, null=True, verbose_name='имеет задолженность')),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['year'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='product',
            name='model_code',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Код модели'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('debt', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dict.client', verbose_name='Наименование клиента')),
                ('model_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dict.product', verbose_name='Модель товара')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
    ]