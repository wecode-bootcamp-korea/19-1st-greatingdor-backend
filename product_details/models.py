from django.db import models

class ProductDetail(models.Model):
    product       = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    content       = models.TextField()
    discount_rate = models.DecimalField(max_digits=18, decimal_places=3)
    store_method  = models.CharField(max_length=10, blank=True, default="")
    capacity      = models.IntegerField()
    kcal          = models.IntegerField()
    is_new        = models.BooleanField()

    class Meta:
        db_table = "product_details"

class ProductDetailImage(models.Model):
    product_detail = models.ForeignKey("ProductDetail", on_delete=models.CASCADE)
    image_url      = models.CharField(max_length=500)

    class Meta:
        db_table = "product_detail_images"

class ProductReview(models.Model):
    product        = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    product_option = models.ForeignKey("products.ProductOption", on_delete=models.CASCADE)
    member         = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    created_at     = models.DateTimeField(auto_now_add=True)
    title          = models.CharField(max_length=100)
    content        = models.CharField(max_length=500)

    class Meta:
        db_table = "product_reviews"

class ProductReviewImage(models.Model):
    product_review = models.ForeignKey("ProductReview", on_delete=models.CASCADE)
    image_url      = models.CharField(max_length=500)

    class Meta:
        db_table = "product_review_images"

class ProductInquiry(models.Model):
    product        = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    title          = models.CharField(max_length=100)
    content        = models.TextField()
    is_public      = models.BooleanField()
    classification = models.CharField(max_length=20)
    email          = models.CharField(max_length=50)
    created_at     = models.DateTimeField(auto_now_add=True)
    member         = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    is_answered    = models.BooleanField()
    answer         = models.TextField(null=True)

    class Meta:
        db_table = "product_inquiries"
