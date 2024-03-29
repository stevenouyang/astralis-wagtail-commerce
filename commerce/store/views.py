import asyncio
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.template.loader import render_to_string
from store.utils.query_utils import get_first_and_second_images
from store.models import Product
from content.models import SliderContent

recommended_products = Product.objects.filter(is_deleted=False, category__is_deleted=False, is_featured=True, product_status="PUBLISHED", in_stock=True)
recommended_products = get_first_and_second_images(recommended_products)

def index_view(request):
    sliders = SliderContent.objects.all()[:5]
    
    context = {
        "recommended_products":recommended_products,
        "sliders": sliders,
    }
    
    return render(request, 'page/store/index.html', context)

def index_view_recommended_filter(request):
    # filter the recommended products based on their category
    pass

def vendor_list_view(request):
    pass

def category_list_view(request):
    pass

def product_list_view(request):
    pass



