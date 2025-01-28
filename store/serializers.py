"""Serializers for store app."""
from rest_framework import serializers
from .models import Products, InventoryProducts, RequestsStoreToInventory, StoreProducts,\
    Orders, OrderItems, Stores, Inventorys

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product."""
    class Meta:
        """Meta class."""
        model = Products
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    """Serializer for Inventory."""
    class Meta:
        """Meta class."""
        model = Inventorys
        fields = '__all__'

class InventoryProductSerializer(serializers.ModelSerializer):
    """Serializer for InventoryProduct."""
    class Meta:
        """ Meta class."""
        model = InventoryProducts
        fields = '__all__'

class RequestsStoreToInventorySerializer(serializers.ModelSerializer):
    """Serializer for RequestsStoreToInventory."""
    class Meta:
        """Meta class."""
        model = RequestsStoreToInventory
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    """Serializer for Store."""
    class Meta:
        """Meta class."""
        model = Stores
        fields = '__all__'

class StoreProductSerializer(serializers.ModelSerializer):
    """Serializer for StoreProduct."""
    class Meta:
        """Meta class."""
        model = StoreProducts
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order."""
    class Meta:
        """Meta class."""
        model = Orders
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for OrderItem."""
    class Meta:
        """Meta class."""
        model = OrderItems
        fields = '__all__'
