from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import *

class SliderContentAdmin(SnippetViewSet):
    model = SliderContent
    menu_label = "Slider Content Admin"
    icon = "image"
    list_display = ["title1", "title2", "created_date"]
    
class ContentSettingAdmin(SnippetViewSetGroup):
    menu_icon = "image"
    menu_label = "Content"
    menu_name = "Content Admin"
    items = (
        SliderContentAdmin,
    )


register_snippet(ContentSettingAdmin)