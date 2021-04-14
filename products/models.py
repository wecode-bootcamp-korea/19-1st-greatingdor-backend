from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    menu  = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name  = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Sub_category(models.Model):
    category  = models.ForeignKey('Category', on_delete=models.CASCADE)
    name      = models.CharField(max_length=45)

    class Meta:
        db_table = 'sub_categories'

class Product(models.Model):
    sub_category  = models.ForeignKey('Sub_category', on_delete=models.CASCADE)
    title         = models.CharField(max_length=200)
    description   = models.CharField(max_length=200)
    price         = models.IntegerField()
    tag           = models.ManyToManyField('Tag', through='Product_tag')

    class Meta:
        db_table = 'products'

class Product_option(models.Model):
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)
    name     = models.CharField(max_length=200)
    price    = models.IntegerField()

    class Meta:
        db_table = 'product_options'

class Tag(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'tags'

class Product_tag(models.Model):
    tag      = models.ForeignKey('Tag', on_delete=models.CASCADE)
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_tags'

class Product_image(models.Model):
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_url  = models.CharField(max_length=500)

    class Meta:
        db_table = 'product_images'

class User_favorite(models.Model):
    member  = models.ForeignKey('members.Member', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_favorites'