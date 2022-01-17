
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken import views

from .views import ConvetApi, CurrencyApi

#app_name = 'api'

urlpatterns = [
    #path('auth/', include('rest_framework.urls')),
    path('convert/', ConvetApi.as_view()),
    path('currency/', CurrencyApi.as_view()),
]