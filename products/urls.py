from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(),name='get_products'),
    path('<int:pk>/', views.ProductDetail.as_view(),name='get_delete_update_product'),
    #re_path(r'^/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(),name='get_delete_update_product'),
]