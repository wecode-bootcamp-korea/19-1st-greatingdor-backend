from django.db import models


class Product_detail(models.Model):
    product       = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    content       = models.TextField()
    discount_rate = models.DecimalField(max_digits=18, decimal_places=3)
    store_method  = models.CharField(max_length=10, null=True)
    capacity      = models.IntegerField()
    kcal          = models.IntegerField()
    is_new        = models.BooleanField()

    class Meta:
        db_table = "product_details"


class Product_detail_image(models.Model):
    product_detail = models.ForeignKey("Product_detail", on_delete=models.CASCADE)
    image_url      = models.CharField(max_length=500)

    class Meta:
        db_table = "product_detail_images"


class Product_review(models.Model):
    product        = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    product_option = models.ForeignKey("products.Product_option", on_delete=models.CASCADE)
    member         = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    insert_at      = models.DateTimeField(auto_now_add=True)
    title          = models.CharField(max_length=45)
    content        = models.CharField(max_length=500)

    class Meta:
        db_table = "product_reviews"


class Product_review_image(models.Model):
    product_review = models.ForeignKey("Product_review", on_delete=models.CASCADE)
    image_url      = models.CharField(max_length=500)

    class Meta:
        db_table = "product_review_images"


class Product_inquiry(models.Model):
    product        = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    title          = models.CharField(max_length=50)
    content        = models.TextField()
    is_public      = models.BooleanField()
    classification = models.CharField(max_length=20)
    email          = models.CharField(max_length=50)
    insert_at      = models.DateTimeField(auto_now_add=True)
    member         = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    is_answered    = models.BooleanField()
    answer         = models.TextField(null=True)

    class Meta:
        db_table = "product_inquiries"
