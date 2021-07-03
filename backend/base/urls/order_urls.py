from django.urls import path
from ..views import order_views

urlpatterns = [
    path('', order_views.getOrders, name='my-orders'),
    path('add/', order_views.addOrderItems, name='orders-add'),
    path('myorders/', order_views.getMyOrders, name='my-orders'),
    path('<str:pk>/deliver/', order_views.updateOrderToDelivered, name='deliverupdate'),
    path('<str:pk>/', order_views.getOrderById, name='order'),
    path('<str:pk>/pay/', order_views.updateOrderToPaid, name='paid-order'),

]
