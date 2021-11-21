from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .seralizers import FoodSerializer
from .models import Food


# Create your views here.
class Foodviewset(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class= FoodSerializer

class FoodDetails(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class= FoodSerializer