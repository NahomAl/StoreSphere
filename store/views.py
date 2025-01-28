"""This module contains the views for the store app."""
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import StoreProducts, InventoryProducts, Products, RequestsStoreToInventory,\
      Orders, OrderItems
from .serializers import StoreProductSerializer, InventoryProductSerializer,\
    ProductSerializer, RequestsStoreToInventorySerializer, OrderSerializer, OrderItemSerializer
from .filters import StoreProductFilter, InventoryProductFilter, ProductFilter, \
    RequestsStoreToInventoryFilter , OrderFilter, OrderItemFilter

class StoreProductViewSet(ModelViewSet):
    """ViewSet for StoreProduct."""
    queryset = StoreProducts.objects.all()
    serializer_class = StoreProductSerializer
    filterset_class = StoreProductFilter


class InventoryProductViewSet(ModelViewSet):
    """ViewSet for InventoryProduct."""
    queryset = InventoryProducts.objects.all()
    serializer_class = InventoryProductSerializer
    filterset_class = InventoryProductFilter


class ProductViewSet(ModelViewSet):
    """ViewSet for Product."""
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class RequestsStoreToInventoryViewSet(ModelViewSet):
    """ViewSet for RequestsStoreToInventory."""
    queryset = RequestsStoreToInventory.objects.all()
    serializer_class = RequestsStoreToInventorySerializer
    filterset_class = RequestsStoreToInventoryFilter

class OrderViewSet(ModelViewSet):
    """ViewSet for Order."""
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter

class OrderItemViewSet(ModelViewSet):
    """ViewSet for OrderItem."""
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer
    filterset_class = OrderItemFilter
