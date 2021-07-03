from django.urls import path
from ..views import product_views

urlpatterns = [
    path('', product_views.getProducts, name='products'),
    path('create-product/', product_views.createProduct, name='create-product'),
    path('upload/', product_views.uploadImage, name='image-product'),
    path('<str:pk>/review/', product_views.createProductReview, name='create-review'),
    path('top/', product_views.getTopProducts, name='product'),
    path('<str:pk>/', product_views.getProduct, name='product'),
    path('delete/<str:pk>/', product_views.deleteProduct, name='delete-product'),
    path('create-product/', product_views.createProduct, name='create-product'),
    path('update/<str:pk>/', product_views.updateProduct, name='update-product'),

]
