from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "menus"

class Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "categories"

class SubCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    name     = models.CharField(max_length=45)

    class Meta:
        db_table = "sub_categories"

class Product(models.Model):
    sub_category = models.ForeignKey("SubCategory", on_delete=models.CASCADE)
    title        = models.CharField(max_length=200)
    description  = models.CharField(max_length=200)
    price        = models.DecimalField(max_digits=20, decimal_places=2)
    tag          = models.ManyToManyField("Tag", through="ProductTag")

    class Meta:
        db_table = "products"

class ProductOption(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    name    = models.CharField(max_length=200)
    price   = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = "product_options"

class Tag(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "tags"

class ProductTag(models.Model):
    tag     = models.ForeignKey("Tag", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "product_tags"

class ProductImage(models.Model):
    product   = models.ForeignKey("Product", on_delete=models.CASCADE)
    image_url = models.CharField(max_length=500)

    class Meta:
        db_table = "product_images"
