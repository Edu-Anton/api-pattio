from rest_framework.generics import ListAPIView

from product.models import Product
from .serializers import ProductSerializer

class ProductListAPIView(ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  