from rest_framework.response import Response
from payment_mode.serializer import PaymentModeSerializer
from payment_mode.models import PaymentMode
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.views import APIView

# Create your views here.
class PaymentModeList(APIView):

    def get(self, request: Request):
        modes = PaymentMode.objects.all()
        serializer = PaymentModeSerializer(modes, many=True)
        return Response(serializer.data)