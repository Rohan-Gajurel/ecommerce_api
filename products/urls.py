from django.urls import path
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, BrandViewSet, CategoriesViewSet

router=DefaultRouter()
router.register(r'product',ProductViewSet,basename='product')
router.register(r'brand',BrandViewSet,basename='brand')
router.register(r'catrgory',CategoriesViewSet,basename='category')

urlpatterns=router.urls
