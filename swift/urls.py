from django.urls import path
from . import views


urlpatterns = [
    path("", views.swiftAccountDetail),
    path("confirm/", views.success_page, name="success_page"),
    
]
