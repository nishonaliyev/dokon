from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Buyurtma
from .serializers import BuyurtmaSerializer

class BuyurtmaListCreateAPIView(ListCreateAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer

class BuyurtmaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
