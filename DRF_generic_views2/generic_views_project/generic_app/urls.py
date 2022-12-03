from django.urls import path
from .views import BankListCreateApi,BankRetriveUpdateDestroyApi

urlpatterns = [
    path('bank/',BankListCreateApi.as_view()),
    path('bank/<int:pk>/',BankRetriveUpdateDestroyApi.as_view())
]