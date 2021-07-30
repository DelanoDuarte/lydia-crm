from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from purchase_opportunity.serializers import PurchaseOpportunityCreateSerializer, PurchaseOpportunityListSerializer

from .models import PurchaseOpportunity, PurchaseOpportunityStatus


# Create your views here.
class PurchaseOpportunityList(APIView):

    def get(self, request: Request):
        opp_status = request.query_params.get('status')
        if opp_status:
            opportunities = PurchaseOpportunity.objects.filter(status=opp_status)
            serializer = PurchaseOpportunityListSerializer(opportunities, many=True)
            return Response(serializer.data)

        opportunities = PurchaseOpportunity.objects.all()
        serializer = PurchaseOpportunityListSerializer(opportunities, many=True)
        return Response(serializer.data)
    
    def post(self, request: Request):
        serializer = PurchaseOpportunityCreateSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOpportunityFind(APIView):

    def get(self, request: Request, id: int):
        opportunity = PurchaseOpportunity.objects.get(id=id)
        serializer = PurchaseOpportunityListSerializer(opportunity)
        return Response(serializer.data)

    def delete(self, request: Request, id: int):
        opportunity = PurchaseOpportunity.objects.get(id=id)
        opportunity.delete()
        return Response(status=HTTP_200_OK)


class PurchaseOpportunityStatusList(APIView):

    def get(self, request: Request):
        all_status = PurchaseOpportunityStatus.values()
        return Response(list(all_status))
