import json

from django.views import View
from django.http  import JsonResponse

from products.models import Product


class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({"MESSAGE": "NOT_FOUND"}, status=404)

            product = Product.objects.get(id=product_id)

            result = {
                "product_id"    : product.id,
                "title"         : product.title,
                "description"   : product.description,
                "price"         : product.price,
                "category_name" : product.category.name,
                "menu_name"     : product.category.menu.name,
                "discount_rate" : product.productdetail_set.first().discount_rate,
                "capacity"      : product.productdetail_set.first().capacity,
                "kcal"          : product.productdetail_set.first().kcal,
                "content"       : product.productdetail_set.first().content,
                "images"        : [
                    product.image_url for product in product.productimage_set.all()
                ],
                "tags"          : [
                    product.tag.name for product in product.producttag_set.all()
                ],
            }

            return JsonResponse({"RESULT": result}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)


class ProductOptionView(View):
    def get(self, request, product_id):
        try:
            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({"MESSAGE": "NOT_FOUND"}, status=404)

            product       = Product.objects.get(id=product_id)
            discount_rate = product.productdetail_set.all().first().discount_rate

            result = [
                {
                    "product_id"   : product_id,
                    "option_id"    : option.id,
                    "option_name"  : option.name,
                    "option_price" : int(option.price * (1 - discount_rate)),
                }
                for option in product.productoption_set.all()
            ]

            return JsonResponse({"RESULT": result}, status=200)
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)