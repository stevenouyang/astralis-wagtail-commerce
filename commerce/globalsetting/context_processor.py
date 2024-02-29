from .models import HeaderTopText
from taggit.models import Tag
from django.db.models import Min, Max, Count

def globalmulti(request):
    # ? Category
    ctx_header_top = HeaderTopText.objects.all()[:4]
    
    context = {
    "ctx_header_top":ctx_header_top,
    }
    
    return context

