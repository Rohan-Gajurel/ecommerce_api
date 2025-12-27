from rest_framework import viewsets
from rest_framework.response import Response
from products.models import Product, Brand, Categories 
from products.serializers import ProductSerializer, BrandSerializer, CategoriesSerializer

class CategoriesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """
    def list(self, request):
        queryset = Categories.objects.all()
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)
    
class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving brand.
    """
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving product.
    """
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)