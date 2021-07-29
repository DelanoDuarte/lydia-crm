from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('find', views.PartnerSearch.as_view(), name='search'),
    path('<int:id>', views.details, name='details'),
    path('partner-type/<int:partner_type_id>', view=views.by_partner_type, name='by_partner_id'),
    path(f'genders', view=views.genders, name='genders')
]   