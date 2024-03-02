from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.admin.panels import TabbedInterface, ObjectList
from .models import *

class SpecTableAdmin(SnippetViewSet):
    model = SpecTable
    menu_label = "SpecTable Admin"
    icon = "list-ul"
    list_display = ["name"]

class CategoryAdmin(SnippetViewSet):
    model = Category
    menu_label = "Category Admin"
    icon = "list-ul"
    list_display = ["title"]
    
class VendorAdmin(SnippetViewSet):
    model = Vendor
    menu_label = "Vendor Admin"
    icon = "group"
    list_display = ["title"]
    
class ProductAdmin(SnippetViewSet):
    model = Product
    menu_label = "Product Admin"
    icon = "pick"
    list_display = ["title"]
    
class StoreSettingAdmin(SnippetViewSetGroup):
    menu_icon = "pick"
    menu_label = "Store"
    menu_name = "Content List"
    items = (
        ProductAdmin, CategoryAdmin, VendorAdmin,
    )


register_snippet(StoreSettingAdmin)
