from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from codetest.currency.models import Convert, Currency
from codetest.api.serializers import (
    ConvertSerializer,
    CurrencySerializer
)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ConvetApi(ListAPIView):
    serializer_class = ConvertSerializer
    queryset = Convert.objects.all()
    pagination_class = LargeResultsSetPagination


class CurrencyApi(ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    pagination_class = LargeResultsSetPagination