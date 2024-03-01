from django.contrib import admin
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from . models import NewsEmail

class NewsEmailAdmin(SnippetViewSet):
    model = NewsEmail
    menu_label = "Newsletter Email"
    icon = "mail"
    list_display = ["email"]
    
class NewsSettingAdmin(SnippetViewSetGroup):
    menu_icon = "mail"
    menu_label = "Newsletter"
    menu_name = "Newsletter"
    items = (
        NewsEmailAdmin,
    )


register_snippet(NewsSettingAdmin)
