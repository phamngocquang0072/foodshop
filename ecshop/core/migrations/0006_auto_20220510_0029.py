# Generated by Django 2.2.14 on 2022-05-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220507_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='imgs/cat_imgs/'),
        ),
    ]