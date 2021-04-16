from django.db import models

class Coupon(models.Model):
    name           = models.CharField(max_length=50)
    code           = models.CharField(max_length=50)
    discount_price = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = "coupons"

class MemberCoupon(models.Model):
    member    = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    coupon    = models.ForeignKey("Coupon", on_delete=models.CASCADE)
    is_use    = models.BooleanField()
    use_order = models.ForeignKey("orders.Order", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "member_coupons"
