from django.db import models

class Order(models.Model):
    to_name               = models.CharField(max_length=45, null=True)
    to_email              = models.CharField(max_length=45, null=True)
    to_phone_number       = models.CharField(max_length=45, null=True)
    reciever_name         = models.CharField(max_length=45, null=True)
    reciever_phone_number = models.CharField(max_length=45, null=True)
    reciever_number       = models.CharField(max_length=45, null=True)
    reciever_message      = models.CharField(max_length=45, null=True)
    shipping_price        = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    member                = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    post_number           = models.CharField(max_length=10, null=True)
    address               = models.CharField(max_length=300, null=True)
    address_detail        = models.CharField(max_length=300, null=True)
    progress_status       = models.CharField(max_length=20)
    created_at            = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"

class OrderProduct(models.Model):
    order          = models.ForeignKey("Order", on_delete=models.CASCADE)
    product        = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    product_option = models.ForeignKey("products.ProductOption", on_delete=models.CASCADE, null=True)
    price          = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    discount_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    quantity       = models.IntegerField()

    class Meta:
        db_table = "order_products"
