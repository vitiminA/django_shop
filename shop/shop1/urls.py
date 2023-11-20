from django.urls import path, include
from .views import IndexView, Index1View, Get_template_names
from .import views
app_name = 'index'
urlpatterns = [
    # path("", views.index, name = 'index'),
    # path("index1/", views.index1, name = 'index1'),
    # path("index2/", views.index2, name = 'index2'),
    path('', IndexView.as_view(), name='index'),
    path('index1/', Index1View.as_view(), name='index1'),
    path('ad_product/', Get_template_names.as_view(), name='ad_product'),
    # path('ad_product', IndexView.as_view(), name='ad_product'),
]