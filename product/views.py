from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from product.serializers import ProductListSerializer, ProductSerializer
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from .models import Product

# Create your views here.
def index(req: HttpRequest):
    if req.method == 'GET':
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ProductSearchView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductSearchByCategoryView(APIView):

    def get(self, request: Request):
        category = request.query_params.get('category')
        products = Product.by_category(category_name=category)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)
