from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.admin.panels import TabbedInterface, ObjectList
from .models import *

class CategoryAdmin(SnippetViewSet):
    model = Category
    menu_label = "Category Admin"
    icon = "list-ul"
    list_display = ["title"]
    
class StoreSettingAdmin(SnippetViewSetGroup):
    menu_icon = "pick"
    menu_label = "Store"
    menu_name = "Content List"
    items = (
        CategoryAdmin,
    )


register_snippet(StoreSettingAdmin)
