from partner.serializers import PartnerListSerializer, PartnerSerializer
from partner.models import Partner
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

# Create your views here.
def index(request: HttpRequest):
    if request.method == 'GET':
        partners = Partner.objects.all()
        serializer = PartnerListSerializer(partners, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PartnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def details(request: HttpRequest, id: int):
    partner = Partner.objects.get(id = id)
    serializer = PartnerSerializer(partner, many=False)
    if serializer.data:
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(serializer.errors, status=400)


def by_partner_type(request: HttpRequest, partner_type_id: int):
    partners = Partner.objects.filter(partnerType__id=partner_type_id)
    serializer = PartnerListSerializer(partners, many=True)
    if serializer.data:
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse(serializer.errors, status=400)
