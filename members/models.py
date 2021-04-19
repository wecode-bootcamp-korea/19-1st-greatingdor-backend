from django.db  import models

class Member(models.Model):
    name             = models.CharField(max_length=50)
    account          = models.CharField(max_length=50)
    password         = models.CharField(max_length=500)
    email            = models.CharField(max_length=50)
    date_birth       = models.DateTimeField()
    phone_number     = models.CharField(max_length=50)
    product_favorite = models.ManyToManyField("products.Product", through="UserFavorite", related_name="favorite")
    coupon           = models.ManyToManyField("coupons.Coupon", through="coupons.MemberCoupon", related_name="coupon")

    class Meta:
        db_table = "members"

class Destination(models.Model):
    member         = models.ForeignKey("Member", on_delete=models.CASCADE)
    address        = models.CharField(max_length=300)
    address_detail = models.CharField(max_length=300)
    post_number    = models.CharField(max_length=10)

    class Meta:
        db_table = "destinations"

class UserFavorite(models.Model):
    member  = models.ForeignKey("Member", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "user_favorites"
