from partner_type.models import PartnerType
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import PartnerTypeSerializer

# Create your views here.
class PartnerTypeList(APIView):

    def get(self, request: Request):
        partners = PartnerType.objects.all()
        serializer = PartnerTypeSerializer(partners, many=True)
        return Response(serializer.data)
    
    def post(self, request: Request):
        pass