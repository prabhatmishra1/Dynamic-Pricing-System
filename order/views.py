# views.py
from rest_framework import viewsets
from .models import Product, SeasonalProduct, BulkProduct, Discount, PercentageDiscount, FixedAmountDiscount, Order
from .serializers import ProductSerializer, SeasonalProductSerializer, BulkProductSerializer, PercentageDiscountSerializer, FixedAmountDiscountSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    Perform CRUD operation for the base product model
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SeasonalProductViewSet(viewsets.ModelViewSet):
    """
    Perform the CRUD operation for the seasonal product
    """
    queryset = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer

class BulkProductViewSet(viewsets.ModelViewSet):
    """
    Perform the CRUD operation for the bulk product
    """
    queryset = BulkProduct.objects.all()
    serializer_class = BulkProductSerializer

class PercentageDiscountViewSet(viewsets.ModelViewSet):
    """
    Perform the CRUD operation for the percentage discount
    """
    queryset = PercentageDiscount.objects.all()
    serializer_class = PercentageDiscountSerializer

class FixedAmountDiscountViewSet(viewsets.ModelViewSet):
    """
    Perform the CRUD operation for the fixed discount
    """
    queryset = FixedAmountDiscount.objects.all()
    serializer_class = FixedAmountDiscountSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    Perform the CRUD operation for the orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
