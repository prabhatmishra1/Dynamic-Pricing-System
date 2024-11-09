# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'seasonal-products', views.SeasonalProductViewSet)
router.register(r'bulk-products', views.BulkProductViewSet)
router.register(r'percentage-discounts', views.PercentageDiscountViewSet)
router.register(r'fixed-discounts', views.FixedAmountDiscountViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
