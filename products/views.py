from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema

from products.models import Product, Brand, Category 
from products.serializers import ProductSerializer, BrandSerializer, CategorySerializer

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """

    queryset = Category.objects.all()
   
      
    serializer_class = CategorySerializer

    @extend_schema(
            request=CategorySerializer,
    )
    def list(self, request):
        
        serializer = CategorySerializer(self.queryset, many=True)
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
    queryset = Product.objects.all()

    @action(
            detail=False,
            methods=['get'], 
            url_path=r'(?P<category>\w+)/all')
    
    def list_product_by_category(self, request, category=None):
        serialized = ProductSerializer(self.queryset.filter(category__name=category))
        return Response(serialized.data)

    serializer_class = ProductSerializer

    @extend_schema(
            request=ProductSerializer,
    )
    def list(self, request):
        serialized = ProductSerializer(self.queryset, many=True)
        return Response(serialized.data)