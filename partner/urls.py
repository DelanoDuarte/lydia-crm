from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.details, name='details'),
    path('partner-type/<int:partner_type_id>', view=views.by_partner_type, name='by_partner_id')
]   