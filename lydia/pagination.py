from rest_framework.pagination import PageNumberPagination

class StandartResultPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100
    display_page_controls=True