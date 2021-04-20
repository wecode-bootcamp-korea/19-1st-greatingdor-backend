import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models          import ProductImage, Product, Menu, Tag, ProductTag, Category

class MainView(View):
    def get(self, request):
        category_id = request.GET.get('category', None)

        if category_id != None:
            products = Product.objects.filter(category_id=category_id)
        else:    
            products = Product.objects.all()
            
        infos  = products.order_by('description')
        result = [{
            'image'      : [image.image_url for image in info.productimage_set.all()],
            'price'      : info.price,
            'title'      : info.title,
            'description': info.description,
            'category'   : info.category.name,
            'isnew'      : info.productdetail_set.all().first().is_new,
            'store'      : info.productdetail_set.all().first().store_method,}
            for info in infos]
            
        page      = int(request.GET.get("page", 1))
        page_size = 6
        limit     = int(page_size * page)
        offset    = int(limit - page_size)
            
        return JsonResponse({'RESULT':result[offset:limit]}, status=200)

class CategoryView(View):
    def get(self, request):
        result = [{
            'menu'     : menu.name,
            'category' : [category.name for category in menu.category_set.all()],}
            for menu in Menu.objects.all()]
        return JsonResponse({'RESULT':result}, status=200)

class SearchView(View):
    def get(self, request):
        search = request.GET.get('search', None)
        
        if search:
            products = Product.objects.filter(Q(title__contains=search) | Q(tag__name=search)).distinct()
        
        if search is None:
            products = Product.objects.all()
        
        result = [{
            'image': [image.image_url for image in product.productimage_set.all()],
            'price': product.price,
            'title': product.title,
            'description': product.description,
            'category': product.category.name,
            'isnew': product.productdetail_set.all().first().is_new,
            'store': product.productdetail_set.all().first().store_method,
            }
            for product in products]
        
        page = int(request.GET.get("page", 1))
        page_size = 6
        limit = int(page_size * page)
        offset = int(limit - page_size)
        return JsonResponse({'RESULT':result[offset:limit]}, status=200)