from rest_framework import serializers
from rest_framework.response import Response
from purchase_opportunity.serializers import PurchaseOpportunityListSerializer
from .models import PurchaseOpportunity, PurchaseOpportunityStatus
from django.shortcuts import render
from rest_framework.request import Request

from rest_framework.views import APIView

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

class PurchaseOpportunityFind(APIView):

    def get(self, request: Request, id: int):
        opportunity = PurchaseOpportunity.objects.get(id=id)
        serializer = PurchaseOpportunityListSerializer(opportunity)
        return Response(serializer.data)

class PurchaseOpportunityStatusList(APIView):

    def get(self, request: Request):
        all_status = PurchaseOpportunityStatus.values()
        return Response(list(all_status))