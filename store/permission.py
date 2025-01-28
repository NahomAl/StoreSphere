"""This module contains the permission classes for the store app."""
from rest_framework.permissions import BasePermission, SAFE_METHODS

class StorePermission(BasePermission):
    """Permission class for Store."""
    def has_permission(self, request, view):
        """Check if the user has permission to access the view."""
        if request.user.is_superuser:
            return True
        return (getattr(request.user, 'role', '') == 'store_manager')


class StoreProductPermission(BasePermission):
    """Permission class for InventoryProduct."""
    def has_permission(self, request, view):
        """Check if the user has permission to access the view."""
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            return True
        else:
            return (getattr(request.user, 'role', '') == 'store_manager')


class InventoryPermission(BasePermission):
    """Permission class for Inventory."""
    def has_permission(self, request, view):
        """Check if the user has permission to access the view."""
        if request.user.is_superuser:
            return True
        return (getattr(request.user, 'role', '') == 'inventory_manager')


class InventoryProductPermission(BasePermission):
    """Permission class for Inventory."""
    def has_permission(self, request, view):
        """Check if the user has permission to access the view."""
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            return (getattr(request.user, 'role', '') in ['store_manager', 'inventory_manager'])
        else:
            return (getattr(request.user, 'role', '') == 'inventory_manager')


class ProductPermission(BasePermission):
    """Permission class for Product."""
    def has_permission(self, request, view):
        """Check if the user has permission to access the view."""
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            return True
        return False

class RequestsStoreToInventoryPermission(BasePermission):
    """Permission class for RequestsStoreToInventory."""
    def has_permission(self, request, view):
        """Check if the user has permission to access the view."""
        if request.user.is_superuser:
            return True
        return (getattr(request.user, 'role', '') in ['store_manager', 'inventory_manager'])

class OrderPermission(BasePermission):
    """Permission class for Order."""
    def has_permission(self, request, view):
        """Check if the user has permission to access the view."""
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated

class OrderItemPermission(BasePermission):
    """Permission class for OrderItem."""
    def has_permission(self, request, view):
        """Check if the user has permission to access the view."""
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated