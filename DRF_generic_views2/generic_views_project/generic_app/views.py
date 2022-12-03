
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import BankSerializer
from .models import Bank

class BankListCreateApi(ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankRetriveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

