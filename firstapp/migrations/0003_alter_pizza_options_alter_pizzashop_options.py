# Generated by Django 4.0.3 on 2022-03-09 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_pizza'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name': 'Пицца', 'verbose_name_plural': 'Пиццы'},
        ),
        migrations.AlterModelOptions(
            name='pizzashop',
            options={'verbose_name': 'Пиццерия', 'verbose_name_plural': 'Пиццерии'},
        ),
    ]
