from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, BrandViewSet, CategoriesViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router=DefaultRouter()
router.register(r'product',ProductViewSet,basename='product')
router.register(r'brand',BrandViewSet,basename='brand')
router.register(r'catrgory',CategoriesViewSet,basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
