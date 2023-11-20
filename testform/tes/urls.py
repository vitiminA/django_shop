from django.urls import path
from .import views

app_name = 'smart'
urlpatterns = [
    path("", views.smart, name='smart'),
    path("savesmart/", views.savesmart, name='savesmart'),
]