from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import (
   HeaderTopText
)

    
class HeaderTopTextSetting(SnippetViewSet):
    model = HeaderTopText
    menu_label = "Header Top Text"
    icon = "list-ul"
    add_to_settings_menu = True
    list_display = ["text",]
    
    
register_snippet(HeaderTopTextSetting)