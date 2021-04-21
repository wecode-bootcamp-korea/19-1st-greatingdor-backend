import json

from django.http  import JsonResponse
from django.views import View

from members.models  import Member
from .models         import Order, OrderProduct
from products.models import Product, ProductOption
from utils           import login_check


class CartView(View):
    @login_check
    def post(self, request):
        try:
            data      = json.loads(request.body)
            member_id = request.member.id
            
            if Order.objects.filter(member_id=member_id).exists():
                order = Order.objects.get(member_id=member_id, progress_status='cart')
            order = Order.objects.create(member_id=member_id, progress_status='cart')
                                   
            if OrderProduct.objects.filter(order_id=order.id, product_id=data['product_id'], product_option_id=data['product_option_id']).exists():
                
                order_product = OrderProduct.objects.get(order_id=order.id, product_id=data['product_id'], product_option_id=data['product_option_id'])
               
                order_product.quantity += data['quantity']
                order_product.save()

                return JsonResponse({'MESSAGE' : 'SUCCESS_UPDATE_QUANTITY'} , status=201)

            OrderProduct.objects.create(
                    order_id          = order.id,
                    product_id        = data['product_id'],
                    product_option_id = data['product_option_id'], 
                    price             = data['price'],
                    discount_price    = data['discount_price'],
                    quantity          = data['quantity'],
                        )
            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status=400)
