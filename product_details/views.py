import json

from django.views import View
from django.http  import JsonResponse

from products.models        import Product
from product_details.models import ProductReview
from product_details.utils  import is_exists_product

class ProductDetailView(View):
    def get(self, request, product_id):

        if not is_exists_product(product_id):
            return JsonResponse({"MESSAGE": "NOT_FOUND"}, status=404)

        product = Product.objects.get(id=product_id)

        result = {
            "id"             : product.id,
            "title"          : product.title,
            "description"    : product.description,
            "price"          : int(product.price),
            "category_name"  : product.category.name,
            "menu_name"      : product.category.menu.name,
            "discount_rate"  : product.productdetail_set.first().discount_rate,
            "discount_price" : int(product.price * (1 - product.productdetail_set.first().discount_rate)),
            "capacity"       : product.productdetail_set.first().capacity,
            "content"        : product.productdetail_set.first().content,
            "images"         : [
                product.image_url for product in product.productimage_set.all()
            ],
            "tags"           : [
                product.tag.name for product in product.producttag_set.all()
            ],
        }

        return JsonResponse({"RESULT": result}, status=200)

class ProductOptionView(View):
    def get(self, request, product_id):

        if not is_exists_product(product_id):
            return JsonResponse({"MESSAGE": "NOT_FOUND"}, status=404)

        product       = Product.objects.get(id=product_id)
        discount_rate = product.productdetail_set.first().discount_rate

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

class ProductReviewView(View):
    def get(self, request, product_id):

        if not is_exists_product(product_id):
            return JsonResponse({"MESSAGE": "NOT_FOUND"}, status=404)

        page = request.GET.get("page", 1)
        page_size = request.GET.get("pageSize", 10)

        limit = int(page * page_size)
        offset = int(limit - page_size)

        result = [
            {
                "title"       : review.title,
                "author"      : review.member.account,
                "created_at"  : review.created_at,
                "option_name" : review.product_option.name,
                "content"     : review.content,
                "images"      : [
                    review.image_url for review in review.productreviewimage_set.all()
                ],
            }
            for review in ProductReview.objects.filter(product_id=product_id).all()[offset:limit]
        ]

        return JsonResponse({"RESULT": result}, status=200)
