from django.urls import path
from .views import BuyurtmaListCreateAPIView, BuyurtmaDetailAPIView

urlpatterns = [
    path('buyurtm,a-berish/', BuyurtmaListCreateAPIView.as_view(), name='buyurtma'),
    path('detail/', BuyurtmaDetailAPIView.as_view(), name ='detail')
]