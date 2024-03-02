from .models import Category, Vendor, Product
from taggit.models import Tag
from django.db.models import Min, Max, Count

def default(request):
    # ? Category
    ctx_categories = Category.objects.filter(is_deleted=False).annotate(product_count=Count('product'))
    ctx_categories_even = []
    ctx_categories_odd = []

    for index, category in enumerate(ctx_categories):
        if index % 2 == 0:
            ctx_categories_even.append(category)
        else:
            ctx_categories_odd.append(category)
            
    # ? Vendor
    ctx_vendors = Vendor.objects.all()[:10]
    ctx_vendors_even = []
    ctx_vendors_odd = []

    for index, vendor in enumerate(ctx_vendors):
        if index % 2 == 0:
            ctx_vendors_even.append(vendor)
        else:
            ctx_vendors_odd.append(vendor)
            
    # ? Vendor
    ctx_tags = Tag.objects.all()[:10]

    
    # ? Address
    # try:
    #     ctx_user_address = Address.objects.get(user=request.user)
    # except:
    #     ctx_user_address=None
    
    
    context = {
    "ctx_categories":ctx_categories,
    "ctx_categories_even":ctx_categories_even,
    "ctx_categories_odd":ctx_categories_odd,
    # "ctx_user_address":ctx_user_address,
    "ctx_vendors": ctx_vendors,
    "ctx_vendors_even": ctx_vendors_even,
    "ctx_vendors_odd": ctx_vendors_odd,
    "ctx_tags":ctx_tags,
    }
    
    return context

