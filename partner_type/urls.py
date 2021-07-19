from django.urls import path
from .views import PartnerTypeList

urlpatterns = [
    path('', PartnerTypeList.as_view())
]