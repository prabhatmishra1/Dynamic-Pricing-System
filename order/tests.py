# tests.py
from django.test import TestCase
from order.models import Product, SeasonalProduct, BulkProduct, PercentageDiscount, FixedAmountDiscount, Order
from rest_framework.test import APIClient
from rest_framework import status


# Model test cases
class ProductModelTestCase(TestCase):
    def test_product_price(self):
        product = Product.objects.create(name="Basic Product", base_price=100.00)
        self.assertEqual(product.get_price(), 100.00)

    def test_seasonal_product_discount(self):
        seasonal_product = SeasonalProduct.objects.create(name="Winter Jacket", base_price=100.00, season_discount=0.10)
        self.assertEqual(seasonal_product.get_price(), 90.00)  # 10% discount

    def test_bulk_product_discount(self):
        bulk_product = BulkProduct.objects.create(name="Household Supplies", base_price=100.00, bulk_discount=0.15)
        self.assertEqual(bulk_product.get_price(), 85.00)  # 15% discount

class DiscountModelTestCase(TestCase):
    def test_percentage_discount(self):
        percentage_discount = PercentageDiscount.objects.create(discount_value=0.20)
        discounted_price = percentage_discount.apply_discount(100.00)
        self.assertEqual(discounted_price, 80.00)  # 20% discount

    def test_fixed_amount_discount(self):
        fixed_discount = FixedAmountDiscount.objects.create(discount_value=15.00)
        discounted_price = fixed_discount.apply_discount(100.00)
        self.assertEqual(discounted_price, 85.00)

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(name="Product 1", base_price=50.00)
        self.product2 = SeasonalProduct.objects.create(name="Seasonal Product", base_price=100.00, season_discount=0.10)
        self.percentage_discount = PercentageDiscount.objects.create(discount_value=0.10)

    def test_order_total_without_discount(self):
        order = Order.objects.create()
        order.products.set([self.product1, self.product2])
        order.calculate_total_price()
        self.assertEqual(order.total_price, 95.00)

    def test_order_total_with_percentage_discount(self):
        order = Order.objects.create(discount=self.percentage_discount)
        order.products.set([self.product1, self.product2])
        order.calculate_total_price()
        self.assertAlmostEqual(order.total_price, 85.50)


#API test cases
class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_seasonal_product(self):
        response = self.client.post('/api/seasonal-products/', {
            "name": "Winter Jacket",
            "base_price": "4000.00",
            "season_discount": 0.10
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Winter Jacket")
        self.assertEqual(float(response.data['base_price']), 4000.00)

    def test_create_bulk_product(self):
        response = self.client.post('/api/bulk-products/', {
            "name": "Household Supplies",
            "base_price": "10000.00",
            "bulk_discount": 0.15
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Household Supplies")
        self.assertEqual(float(response.data['base_price']), 10000.00)

class DiscountAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_percentage_discount(self):
        response = self.client.post('/api/percentage-discounts/', {
            "discount_value": 0.05
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['discount_value'], 0.05)

    def test_create_fixed_discount(self):
        response = self.client.post('/api/fixed-discounts/', {
            "discount_value": 100.00
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(float(response.data['discount_value']), 100.00)

class OrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product1 = Product.objects.create(name="Basic Product", base_price=100.00)
        self.seasonal_product = SeasonalProduct.objects.create(name="Winter Jacket", base_price=200.00, season_discount=0.10)
        self.percentage_discount = PercentageDiscount.objects.create(discount_value=0.05)

    def test_create_order_without_discount(self):
        response = self.client.post('/api/orders/', {
            "products": [
                {"id": self.product1.id},
                {"id": self.seasonal_product.id}
            ]
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('total_price', response.data)

    def test_create_order_with_discount(self):
        response = self.client.post('/api/orders/', {
            "products": [
                {"id": self.product1.id},
                {"id": self.seasonal_product.id}
            ],
            "discount": {
                "id": self.percentage_discount.id
            }
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('total_price', response.data)
