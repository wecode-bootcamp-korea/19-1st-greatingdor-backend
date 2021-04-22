from products.models import Product

def is_exists_product(product_id):
    return Product.objects.filter(id=product_id).exists()