# Generated by Django 3.2 on 2021-04-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_sub_category_product_category'),
        ('members', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='product_cart',
        ),
        migrations.AlterField(
            model_name='member',
            name='product_favorite',
            field=models.ManyToManyField(related_name='favorite', through='members.UserFavorite', to='products.Product'),
        ),
    ]
