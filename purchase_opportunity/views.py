from django.shortcuts import render
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from purchase_opportunity.serializers import PurchaseOpportunityListSerializer

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
