import json

from django.http      import JsonResponse
from django.views     import View

from members.models  import Member
from .models         import Order, OrderProduct
from utils           import login_check


class CartView(View):
    @login_check
    def post(self, request):
        try:
            data              = json.loads(request.body)
            member_id         = request.member.id
            product_id        = data['product_id']
            product_option_id = data['product_option_id']
            quantity          = data['quantity']
            
            cart, created = Order.objects.get_or_create(member_id=member_id, progress_status='cart')
            
            if not created:
                order = Order.objects.get(member_id=member_id, progress_status='cart')
            order = Order.objects.get(member_id=member_id, progress_status='cart')

            if OrderProduct.objects.filter(order_id=order.id, product_id=product_id, product_option_id=product_option_id).exists():
               
               order_product = OrderProduct.objects.get(order_id=order.id, product_id=product_id, product_option_id=product_option_id)
              
               order_product.quantity += quantity
               order_product.save()

               return JsonResponse({'MESSAGE' : 'SUCCESS'} , status=201)

            OrderProduct.objects.create(
                    order_id          = order.id,
                    product_id        = product_id,
                    product_option_id = product_option_id, 
                    quantity          = quantity
                        )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)


    @login_check
    def get(self, request):
        member_id = request.member.id
        order_products = Order.objects.get(member_id=member_id, progress_status='cart').orderproduct_set.all()
        carts = [
                {
                    'order_product_id'  : order_product.id,
                    'product_id'        : order_product.product.id,
                    'product_option_id' : order_product.product_option.id,
                    'option_name'       : order_product.product_option.name,
                    'product_title'     : order_product.product.title,
                    'quantity'          : order_product.quantity,
                    'price'             : order_product.product.price,
                    'discount_rate'     : order_product.product.productdetail_set.first().discount_rate,
                    'image_url'         : order_product.product.productimage_set.first().image_url
                } for order_product in order_products
            ]
        return JsonResponse({'MESSAGE' : 'SUCCESS', 'order_products' : carts}, status=201)


    @login_check
    def delete(self, request):
        data      = json.loads(request.body)
        member_id = request.member.id

        OrderProduct.objects.get(order__member_id=member_id, product_id=data['product_id']).delete()

        return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)











