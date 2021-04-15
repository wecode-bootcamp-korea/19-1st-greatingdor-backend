from django.db import models

class Cart(models.Model):
    product        = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="cart_product")
    product_option = models.ForeignKey("products.ProductOption", on_delete=models.CASCADE, null=True)
    quantity       = models.IntegerField()
    member         = models.ForeignKey("members.Member", on_delete=models.CASCADE)

    class Meta:
        db_table = "carts"

class Order(models.Model):
    to_name               = models.CharField(max_length=45)
    to_email              = models.CharField(max_length=45)
    to_phone_number       = models.CharField(max_length=45)
    reciever_name         = models.CharField(max_length=45)
    reciever_phone_number = models.CharField(max_length=45)
    reciever_number       = models.CharField(max_length=45)
    reciever_message      = models.CharField(max_length=45)
    shipping_price        = models.DecimalField(max_digits=20, decimal_places=2)
    member                = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    post_number           = models.CharField(max_length=10)
    address               = models.CharField(max_length=300)
    address_detail        = models.CharField(max_length=300)
    progress_status       = models.CharField(max_length=20)
    created_at            = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"

class OrderProduct(models.Model):
    order          = models.ForeignKey("Order", on_delete=models.CASCADE)
    product        = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    product_option = models.ForeignKey("products.ProductOption", on_delete=models.CASCADE)
    price          = models.DecimalField(max_digits=20, decimal_places=2)
    discount_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity       = models.IntegerField()

    class Meta:
        db_table = "order_products"
