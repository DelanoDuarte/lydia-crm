from django.urls import path
from .views import PurchaseOpportunityFind, PurchaseOpportunityList, PurchaseOpportunityStatusList

urlpatterns = [
    path('', view=PurchaseOpportunityList.as_view()),
    path('<int:id>', view=PurchaseOpportunityFind.as_view()),
    path('status/all', view=PurchaseOpportunityStatusList.as_view())
]