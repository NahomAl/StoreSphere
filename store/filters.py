"""Filter classes for the models in the store app"""
from django_filters.rest_framework import FilterSet, CharFilter
from .models import StoreProducts, InventoryProducts, Products, RequestsStoreToInventory, \
    Orders, OrderItems

class StoreProductFilter(FilterSet):
    """Filter class for StoreProduct."""
    class Meta:
        """Meta class for StoreProduct."""
        model = StoreProducts
        fields = {
            'quantity': ['exact', 'lt', 'gt'],
            'store': ['exact'],
            'product': ['exact']
        }

class InventoryProductFilter(FilterSet):
    """Filter class for InventoryProduct."""
    class Meta:
        """Meta class for InventoryProduct."""
        model = InventoryProducts
        fields = {
            'quantity': ['exact', 'lt', 'gt'],
            'inventory': ['exact'],
            'product': ['exact']
        }

class ProductFilter(FilterSet):
    """Filter class for Product."""
    name = CharFilter(lookup_expr='icontains')
    class Meta:
        """Meta class for Product."""
        model = Products
        fields = {
            'stock': ['exact', 'lt', 'gt'],
            'selling_price': ['exact', 'lt', 'gt'],
            'name': ['exact']
        }

class RequestsStoreToInventoryFilter(FilterSet):
    """Filter class for RequestsStoreToInventory."""
    class Meta:
        """Meta class for RequestsStoreToInventory."""
        model = RequestsStoreToInventory
        fields = {
            'status': ['exact'],
            'store': ['exact'],
            'inventory': ['exact']
        }

class OrderFilter(FilterSet):
    """Filter class for Order."""
    class Meta:
        """Meta class for Order."""
        model = Orders
        fields = {
            'status': ['exact'],
            'store': ['exact']
        }

class OrderItemFilter(FilterSet):
    """Filter class for OrderItem."""
    class Meta:
        """Meta class for OrderItem."""
        model = OrderItems
        fields = {
            'order': ['exact'],
            'product': ['exact']
        }
