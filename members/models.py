from django.db import models
from products.models import Product

class Member(models.Model):
    name         = models.CharField(max_length=50)
    account      = models.CharField(max_length=50)
    password     = models.CharField(max_length=500)
    email        = models.CharField(max_length=50)
    date_birth   = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    coupon       = models.ManyToManyField('coupons.Coupon', through='coupons.Member_coupon', related_name='coupon')
    product_fav  = models.ManyToManyField('products.Product', through='products.User_favorite', related_name='favorite')
    product_cart = models.ManyToManyField('products.Product', through='orders.Cart', related_name='cart')

    class Meta:
        db_table = 'members'

class Destination(models.Model):
    member         = models.ForeignKey('Member', on_delete=models.CASCADE)
    address        = models.CharField(max_length=300)
    address_detail = models.CharField(max_length=300)
    post_number    = models.IntegerField()

    class Meta:
        db_table = 'destinations'
