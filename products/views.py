import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models          import ProductImage, Product, Menu, Tag, ProductTag, Category

class MainView(View):
    def get(self, request):
        category_id = request.GET.get('category')
        search      = request.GET.get('search')
        tag_list    = request.GET.getlist('tag')
        ex_tag_list = request.GET.getlist('ex_tag')
        food_list   = request.GET.getlist('food')
        
        if category_id:
            products = Product.objects.filter(category_id=category_id)
            
        if search:
            products = Product.objects.filter(Q(title__contains=search) | Q(tag__name=search)).distinct()
        
        if category_id is None and search is None:
            q = Q()
            if tag_list:
                q.add(Q(tag__id__in=tag_list), q.OR)
            
            if food_list:
                q.add(Q(category_id__in=food_list), q.AND)

            if ex_tag_list:
                q.add(~Q(tag__id__in=ex_tag_list), q.AND)
            products = Product.objects.filter(q).distinct()
            
        infos  = products.order_by('description')
        
        result = [{
            'id'         : info.id,
            'image'      : [image.image_url for image in info.productimage_set.all()],
            'price'      : info.price,
            'title'      : info.title,
            'description': info.description,
            'category'   : info.category.name,
            'isnew'      : info.productdetail_set.first().is_new,
            'store'      : info.productdetail_set.first().store_method,}
            for info in infos]
            
        page      = int(request.GET.get("page", 1))
        page_size = 6
        limit     = int(page_size * page)
        offset    = int(limit - page_size)
            
        return JsonResponse({'RESULT':result}, status=200)

class CategoryView(View):
    def get(self, request):
        result = [{
            'menu'     : menu.name,
            'category' : [category.name for category in menu.category_set.all()]}
            for menu in Menu.objects.all()]
        return JsonResponse({'RESULT':result}, status=200)