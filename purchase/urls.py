from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.PurchaseList.as_view()),
    path('partner/<int:id>', view=views.PurchaseByPartner.as_view())
]