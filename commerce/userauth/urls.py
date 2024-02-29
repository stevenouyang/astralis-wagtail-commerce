from django.urls import include, path
from . import views
# from .views_api import <>

app_name = 'userauth'

urlpatterns = [
    # endpoint: MONOLITH
    path("signup/", views.register_view, name="sign-up"),
    path("signin/", views.login_view, name="sign-in"),
    path("signout/", views.logout_view, name="sign-out"),
    
    # endpoint: REST API
    
]
