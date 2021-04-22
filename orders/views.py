import json

from django.http      import JsonResponse
from django.views     import View

from members.models   import Member
from .models          import Order, OrderProduct
from utils            import login_check

class CartView(View):
    @login_check
    def post(self, request):
        try:
            data              = json.loads(request.body)
            member_id         = request.member.id
            product_id        = data['product_id']
            product_option_id = data['product_option_id']
            quantity          = data['quantity']
            
            order_product, order_product_created = Order.objects.get_or_create(member_id=member_id, progress_status='cart')
            
            if order_product.orderproduct_set.filter(product_id=product_id).exist():
                user_cart           = user_order.orderproduct_set.get(product_id = product_id)
                user_cart.quantity += int(quantity)
                user_cart.save()
            
            else:
                user_cart = order_product.orderproduct_set.create(
                        order_id          = order.id,
                        product_id        = product_id,
                        product_option_id = product_option_id,
                        quantity          = quantity,
                        )
                
            return JsonResponse({'MESSAGE': 'SUCCESS'}, status = 201)
        except Order.MultipleObjectsReturned:
            return JsonResponse({'ERROR': "MORE_OBJECTS"}, status = 400)