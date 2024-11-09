# serializers.py
from rest_framework import serializers
from order.models import (Product, SeasonalProduct, BulkProduct,
        Discount, PercentageDiscount, FixedAmountDiscount, Order)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'base_price']

class SeasonalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonalProduct
        fields = ['id', 'name', 'base_price', 'season_discount']

class BulkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkProduct
        fields = ['id', 'name', 'base_price', 'bulk_discount']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'discount_value']

class PercentageDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PercentageDiscount
        fields = ['id', 'discount_value']

class FixedAmountDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedAmountDiscount
        fields = ['id', 'discount_value']

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    discount = DiscountSerializer(required=False)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'products', 'discount', 'total_price']
