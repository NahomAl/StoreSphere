"""This module is used to register the models in the admin panel."""
from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.admin import register
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from unfold.forms import AdminPasswordChangeForm , UserChangeForm, UserCreationForm
from unfold.admin import TabularInline
from .models import Products, Inventorys, InventoryProducts, \
    Stores, StoreProducts, RequestsStoreToInventory, Orders, \
        OrderItems

admin.site.unregister(User)
admin.site.unregister(Group)
@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    """User model admin."""
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

@register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    """Group model admin."""

@register(Products)
class ProductsAdmin(ModelAdmin):
    """Products model admin."""
    list_display = ('name', 'buying_price', 'selling_price',
                    'stock', 'created', 'available')
    search_fields = ('name', 'selling_price', 'stock', 'created')
    list_filter = ('name', 'stock', 'created', 'available', 'selling_price', 'buying_price')
    actions = ['make_available', 'make_unavailable']

    def get_fields(self, request, obj=None):
        fields = ['name', 'description', 'selling_price', 'available']
        if not obj:  # If the object is being created
            fields.insert(2, 'buying_price')
        return fields

    def make_available(self, request, queryset):
        queryset.update(available=True)
    make_available.short_description = "Mark selected products as available"

    def make_unavailable(self, request, queryset):
        queryset.update(available=False)
    make_unavailable.short_description = "Mark selected products as unavailable"


@register(Inventorys)
class InventorysAdmin(ModelAdmin):
    """Inventorys model admin."""
    list_display = ('name', 'location', 'manager', 'created')
    fields = ('name', 'location', 'manager')
    search_fields = ('name', 'location', 'manager')
    list_filter = ('name', 'location', 'created')


@register(InventoryProducts)
class InventoryProductsAdmin(ModelAdmin):
    """InventoryProducts model admin."""
    list_display = ('inventory', 'product', 'quantity', 'created')
    fields = ('inventory', 'product', 'quantity')
    search_fields = ('inventory', 'product')
    list_filter = ('inventory', 'product', 'created')


@register(Stores)
class StoresAdmin(ModelAdmin):
    """Stores model admin."""
    list_display = ('name', 'location', 'manager', 'created')
    fields = ('name', 'location', 'manager')
    search_fields = ('name', 'location', 'manager')
    list_filter = ('name', 'location', 'created')


@register(StoreProducts)
class StoreProductsAdmin(ModelAdmin):
    """StoreProducts model admin."""
    list_display = ('store', 'product', 'quantity', 'created')
    fields = ('store', 'product', 'quantity')
    search_fields = ('store', 'product')
    list_filter = ('store', 'product', 'created')


class OrderItemsInline(TabularInline):
    """OrderItems inline admin."""
    model = OrderItems
    extra = 1

@register(Orders)
class OrdersAdmin(ModelAdmin):
    """Orders model admin."""
    list_display = ('id', 'store', 'total', 'status', 'payment', 'created')
    fields = ('store', 'status', 'payment')
    search_fields = ('store', 'status', 'payment')
    list_filter = ('store', 'status', 'payment', 'created')
    inlines = [OrderItemsInline]


@register(OrderItems)
class OrderItemsAdmin(ModelAdmin):
    """OrderItems model admin."""
    list_display = ('order', 'product', 'quantity', 'total', 'created')
    fields = ('order', 'product', 'quantity')
    search_fields = ('order', 'product')
    list_filter = ('order', 'product', 'created')


@register(RequestsStoreToInventory)
class RequestsStoreToInventoryAdmin(ModelAdmin):
    """RequestsStoreToInventory model admin."""
    list_display = ('store', 'inventory', 'product',
                    'quantity', 'status', 'created')
    fields = ('store', 'inventory', 'product', 'quantity', 'status')
    search_fields = ('store', 'inventory',
                     'product', 'status')
    list_filter = ('store', 'inventory', 'product', 'status', 'created')
