import asyncio
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.template.loader import render_to_string

def index_view(request):
    # products = Product.objects.filter(is_deleted=False, category__is_deleted=False, is_featured=True, product_status="PUBLISHED", in_stock=True)
    # products = get_first_and_second_images(products)
    
    context = {
        # "products":products,
    }
    
    return render(request, 'page/store/index.html', context)