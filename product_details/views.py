import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import F

from products.models        import Product, ProductImage
from product_details.models import ProductDetail


class ProductDetailView(View):
    def get(self, request):
        try:
            product_id = request.GET["productId"]

            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({"MESSAGE": "NOT_FOUND"}, status=404)

            result = (
                ProductDetail.objects.filter(product_id=product_id)
                .annotate(
                    menu_name     = F("product__category__menu__name"),
                    category_name = F("product__category__name"),
                    title         = F("product__title"),
                    description   = F("product__description"),
                    price         = F("product__price"),
                )
                .values(
                    "menu_name",
                    "category_name",
                    "title",
                    "description",
                    "price",
                    "content",
                    "discount_rate",
                    "capacity",
                    "kcal",
                )
                .first()
            )

            result["images"] = [
                image.image_url
                for image in ProductImage.objects.filter(product_id=product_id)
            ]

            result["tags"] = [
                tag["tag__name"]
                for tag in Product.objects.filter(id=product_id).values("tag__name")
            ]

            return JsonResponse({"RESULT": result}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
