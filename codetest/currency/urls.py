
from django.urls import path
from .views import IndexView, DataTable
app_name = 'currency'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('list/', DataTable.as_view(), name='currency_table')
]