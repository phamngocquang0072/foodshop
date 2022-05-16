# Generated by Django 2.2.14 on 2022-05-11 17:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20220510_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '1.Category'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': '3.Customers'},
        ),
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name_plural': '6.Favourite'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': '6.News'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': '4.Order'},
        ),
        migrations.AlterModelOptions(
            name='orderdetail',
            options={'verbose_name_plural': '5.Order Detail'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '2.Product'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_date',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]