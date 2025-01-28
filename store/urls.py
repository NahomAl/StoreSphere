""" store URL Configuration """
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  StoreProductViewSet, InventoryProductViewSet,\
      ProductViewSet, RequestsStoreToInventoryViewSet, OrderViewSet,\
        OrderItemViewSet

router = DefaultRouter()
router.register('store_products', StoreProductViewSet)
router.register('inventory_products', InventoryProductViewSet)
router.register('products', ProductViewSet)
router.register('requests_store_to_inventory', RequestsStoreToInventoryViewSet)
router.register('orders', OrderViewSet)
router.register('order_items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]