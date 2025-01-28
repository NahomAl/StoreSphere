"""This module contains the views for the store app."""
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import StoreProducts, InventoryProducts, Products, RequestsStoreToInventory,\
      Orders, OrderItems, Stores, Inventorys

from .serializers import StoreProductSerializer, InventoryProductSerializer,\
    ProductSerializer, RequestsStoreToInventorySerializer, OrderSerializer, OrderItemSerializer,\
    StoreSerializer, InventorySerializer

from .filters import StoreProductFilter, InventoryProductFilter, ProductFilter, \
    RequestsStoreToInventoryFilter , OrderFilter, OrderItemFilter, StoreFilter, InventoryFilter

from .permission import  StoreProductPermission, InventoryProductPermission, \
    ProductPermission, RequestsStoreToInventoryPermission, OrderPermission, OrderItemPermission,\
    StorePermission, InventoryPermission

class StoreViewSet(ModelViewSet):
    """ViewSet for Store."""
    permission_classes = [StorePermission]
    queryset = Stores.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StoreFilter

class StoreProductViewSet(ModelViewSet):
    """ViewSet for StoreProduct."""
    permission_classes = [StoreProductPermission]
    queryset = StoreProducts.objects.all()
    serializer_class = StoreProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StoreProductFilter


class InventoryViewSet(ModelViewSet):
    """ViewSet for Inventory."""
    permission_classes = [InventoryPermission]
    queryset = Inventorys.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InventoryFilter


class InventoryProductViewSet(ModelViewSet):
    """ViewSet for InventoryProduct."""
    permission_classes = [InventoryProductPermission]
    queryset = InventoryProducts.objects.all()
    serializer_class = InventoryProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InventoryProductFilter


class ProductViewSet(ModelViewSet):
    """ViewSet for Product."""
    permission_classes = [ProductPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class RequestsStoreToInventoryViewSet(ModelViewSet):
    """ViewSet for RequestsStoreToInventory."""
    permission_classes = [RequestsStoreToInventoryPermission]
    queryset = RequestsStoreToInventory.objects.all()
    serializer_class = RequestsStoreToInventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RequestsStoreToInventoryFilter

class OrderViewSet(ModelViewSet):
    """ViewSet for Order."""
    permission_classes = [OrderPermission]
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

class OrderItemViewSet(ModelViewSet):
    """ViewSet for OrderItem."""
    permission_classes = [OrderItemPermission]
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderItemFilter
