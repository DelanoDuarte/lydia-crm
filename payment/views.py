from rest_framework.pagination import LimitOffsetPagination
from payment.serializer import PaymentCreateSerializer, PaymentListSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from payment.models import Payment

# Create your views here.
class PaymentList(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request: Request):
        serializer = PaymentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
