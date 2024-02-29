from django.urls import include, path
from . import views
# from .views_api import <>

app_name = "store"

urlpatterns = [
    # endpoint: MONOLITH
    path("", views.index_view, name="index"),
    
    # endpoint: REST API
    
]
