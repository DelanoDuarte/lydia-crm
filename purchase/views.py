from purchase.models import Purchase
from purchase.serializers import PurchaseCreateSerializer, PurchaseSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class PurchaseList(APIView):

    def get(self, request: Request, format=None):
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data) 
    
    def post(self, request: Request, format=None):
        serializer = PurchaseCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
