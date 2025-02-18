"""Model definitions."""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class User(AbstractUser):
    """Model definition for Users."""
    role = models.CharField(max_length=20, choices=(('admin', 'Admin'), ('inventory_manger',
                            'Inventory_Manager'), ('store_manager', 'Store_Manager'), ('salesman', 'Salesman')))
class Products(models.Model):
    """Model definition for Products."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    buying_price = models.FloatField()
    selling_price = models.FloatField()
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.available = False
        else:
            self.available = True
        if self.stock < 0:
            raise ValidationError("The stock cannot be negative.")
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for Products."""
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Inventorys(models.Model):
    """Model definition for Inventory."""
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.name)

    class Meta:
        """Meta definition for Inventory."""
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'


class InventoryProducts(models.Model):
    """Model definition for Inventory."""
    inventory = models.ForeignKey(Inventorys, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.product)

    def save(self, *args, **kwargs):
        product = Products.objects.get(pk=self.product.pk)
        if self.pk is None:
            product.stock += self.quantity
            product.save()
        else:
            old_quantity = InventoryProducts.objects.get(pk=self.pk).quantity
            product.stock += self.quantity - old_quantity
        product.save()
        if self.quantity < 0:
            raise ValidationError("The quantity cannot be negative.")
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for Inventory."""
        verbose_name = 'Inventory Product'
        verbose_name_plural = 'Inventories Products'
        constraints = [
            models.UniqueConstraint(
                fields=['inventory', 'product'], name='unique_inventory_product')
        ]


class Stores(models.Model):
    """Model definition for Stores."""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.name)

    class Meta:
        """Meta definition for Stores."""
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'


class StoreProducts(models.Model):
    """Model definition for StoresProduct."""
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.product)

    def save(self, *args, **kwargs):
        product = Products.objects.get(pk=self.product.pk)
        if self.pk is None:
            product.stock += self.quantity
            product.save()
        else:
            old_quantity = StoreProducts.objects.get(pk=self.pk).quantity
            product.stock += self.quantity - old_quantity
        product.save()
        if self.quantity < 0:
            raise ValidationError("The quantity cannot be negative.")
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for StoresProduct."""
        verbose_name = 'Store Product'
        verbose_name_plural = 'Stores Products'
        constraints = [
            models.UniqueConstraint(
                fields=['store', 'product'], name='unique_store_product')
        ]


class RequestsStoreToInventory(models.Model):
    """Model definition for RequestsStoreToInventory."""
    CHOICES = (('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'))
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventorys, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.product)
    
    def save(self, *args, **kwargs):
        if self.quantity < 0:
            raise ValidationError("The quantity cannot be negative.")
        if self.pk is not None:
            old_status = RequestsStoreToInventory.objects.get(pk=self.pk).status
            if old_status in ['approved', 'rejected']:
                raise ValidationError("The request is already processed.")
            if old_status != 'approved' and self.status == 'approved':
                inventory_product = InventoryProducts.objects.filter(
                    inventory=self.inventory, product=self.product)
                if inventory_product.exists():
                    inventory_product = inventory_product.first()
                    if inventory_product.quantity < self.quantity:
                        raise ValidationError("The quantity is not available in the inventory.")
                    inventory_product.quantity -= self.quantity
                    inventory_product.save()
                store_product = StoreProducts.objects.filter(
                    store=self.store, product=self.product)
                if store_product.exists():
                    store_product = store_product.first()
                    store_product.quantity += self.quantity
                    store_product.save()
                else:
                    StoreProducts.objects.create(
                        store=self.store, product=self.product, quantity=self.quantity)
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for RequestsStoreToInventory."""
        verbose_name = 'RequestsStoreToInventory'
        verbose_name_plural = 'RequestsStoreToInventories'


class Orders(models.Model):
    """Model definition for Orders."""
    CHOICES = (('pending', 'Pending'), ('paid', 'Paid'), ('canceled', 'Canceled'))
    PAYMENT_CHOICES = (('cash', 'Cash'), ('telebirr', 'Telebirr'), ('cbe', 'CBE'))
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=CHOICES, default='pending')
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cash')
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.store)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_status = Orders.objects.get(pk=self.pk).status
            if old_status in ['paid', 'canceled']:
                raise ValidationError("The order is already processed.")
            if old_status != 'paid' and self.status == 'paid':
                order_items = OrderItems.objects.filter(order=self)
                for item in order_items:
                    store_products = StoreProducts.objects.filter(
                        store=self.store, product=item.product)
                    for store_product in store_products:
                        store_product.quantity -= item.quantity
                        store_product.save()
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for Orders."""
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class OrderItems(models.Model):
    """Model definition for OrderItems."""
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    def __str__(self):
        return str(self.order)

    def save(self, *args, **kwargs):
        order = Orders.objects.get(pk=self.order.pk)
        if order.status in ['paid', 'canceled']:
            raise ValidationError("The order is already processed.")
        if self.pk is None:
            store_product = StoreProducts.objects.get(
                store=self.order.store, product=self.product)
            if store_product.quantity < self.quantity:
                raise ValidationError(
                    "The quantity is not available in the store.")
            self.total = self.product.selling_price * self.quantity
        #update order total
        order.total += self.total
        order.save()
        super().save(*args, **kwargs)
    class Meta:
        """Meta definition for OrderItems."""
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

@receiver(pre_delete, sender=StoreProducts or InventoryProducts)
def update_stock(sender, instance, **kwargs):
    product = Products.objects.get(pk=instance.product.pk)
    product.stock -= instance.quantity
    product.save()
