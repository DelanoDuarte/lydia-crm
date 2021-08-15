from lydia.pagination import StandartResultPagination
from purchase.models import Purchase
from purchase.serializers import PurchaseCreateSerializer, PurchaseSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
  
class PurchaseList(ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    pagination_class = StandartResultPagination

    def post(self, request: Request, format=None):
        serializer = PurchaseCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
