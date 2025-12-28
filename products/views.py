from rest_framework import viewsets
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from products.models import Product, Brand, Categories 
from products.serializers import ProductSerializer, BrandSerializer, CategoriesSerializer

class CategoriesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """
    serializer_class = CategoriesSerializer
    @extend_schema(
            request=CategoriesSerializer,
    )
    def list(self, request):
        queryset = Categories.objects.all()
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)
    
class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving brand.
    """
    serializer_class = BrandSerializer

    @extend_schema(
            request=BrandSerializer,
    )
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving product.
    """
    serializer_class = ProductSerializer

    @extend_schema(
            request=ProductSerializer,
    )
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)