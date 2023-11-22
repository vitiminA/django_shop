from django.urls import path, include
from .views import IndexView, Index1View, Get_template_names, delete_product, edit_product
from .import views
app_name = 'index'
urlpatterns = [
    # path("", views.index, name = 'index'),
    # path("index1/", views.index1, name = 'index1'),
    # path("index2/", views.index2, name = 'index2'),
    path('', IndexView.as_view(), name='index'),
    path('index1/', Index1View.as_view(), name='index1'),
    path('ad_product/', Get_template_names.as_view(), name='ad_product'),
    path('edit_product/<int:product_id>/',views.edit_product, name ='edit_product'),
    path('delete_product/<int:product_id>/',views.delete_product, name ='delete_product'),
]