import json

from django.http  import JsonResponse
from django.views import View

from .models      import ProductImage, Product, Menu, Tag, ProductTag

class MainView(View):
    def get(self, request):
        category_id = request.GET.get('category', None)

        if category_id != None:
            infos  = Product.objects.filter(category_id=category_id)
        else:    
            infos  = Product.objects.all()

        page = int(request.GET.get("page", 1))
        page_size = 6
        limit = int(page_size * page)
        offset = int(limit - page_size)
        
        result = []
        for info in infos:
            images  = info.productimage_set.all()
            image_list = [image.image_url for image in images]
            result.append(
            {
            'image': image_list,
            'price': info.price,
            'title': info.title,
            'description': info.description,
            'category': info.category.name,
            'isnew': True
            }
            )
        return JsonResponse({'RESULT':result[offset:limit]}, status=200)

class CategoryView(View):
    def get(self, request):
        menus = Menu.objects.all()
        result = []
        for menu in menus:
            categories = menu.category_set.all()
            category_list = []
            for category in categories:
                category_list.append(category.name)
            result.append(
            {
            'menu': menu.name,
            'category': category_list,
            }
            )
        return JsonResponse({'RESULT':result}, status=200)