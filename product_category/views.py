from product_category.serializers import ProductCategorySerializer
from product_category.models import ProductCategory
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
def index(request: HttpRequest):
    if request.method == 'GET':
        product_categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(product_categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)