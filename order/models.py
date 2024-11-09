# models.py
from django.db import models

class Product(models.Model):
    """
    Base model for all products.
    """
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self):
        return self.base_price

    def __str__(self):
        return f"{self.name} - {self.base_price}"

class SeasonalProduct(Product):
    """
    Model for products with seasonal discounts.
    """
    season_discount = models.FloatField(help_text="Discount rate as a decimal (e.g., 0.10 for 10%)")

    def get_price(self):
        return max(0, self.base_price *(1- self.season_discount))

class BulkProduct(Product):
    """
    Model for products with bulk discounts.
    """
    bulk_discount = models.FloatField(help_text="Discount rate as a decimal (e.g., 0.15 for 15%)")

    def get_price(self):
        return max(0, self.base_price * (1 - self.bulk_discount))

class Discount(models.Model):
    """
    Base class for discounts.
    """
    discount_value = models.FloatField(help_text="Discount value as a decimal (e.g., 0.05 for 5%)")

    def apply_discount(self, price):
        raise NotImplementedError("Subclasses must implement this method")

class PercentageDiscount(Discount):
    """
    Model for percentage-based discounts.
    """
    def apply_discount(self, price):
        return max(0, price * (1 - self.discount_value))

class FixedAmountDiscount(Discount):
    """
    Model for fixed amount discounts.
    """
    def apply_discount(self, price):
        return max(0, price - self.discount_value)

class Order(models.Model):
    """
    Model to represent an order with products and an optional discount.
    """
    products = models.ManyToManyField(Product)
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0.00)

    def calculate_total_price(self):
        # Calculate base total from products
        total = sum(product.get_price() for product in self.products.all())

        # Apply discount if available
        if self.discount:
            total = self.discount.apply_discount(total)

        # Update total_price field
        self.total_price = total
        self.save()
        return self.total_price

    def save(self, *args, **kwargs):
        # Automatically calculate the total price before saving
        self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} - Total Price: {self.total_price}"
