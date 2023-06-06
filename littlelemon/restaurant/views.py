from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import menu, booking
from .serializer import MenuItemSerializer, BookingSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemsView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer
    pass

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer
    pass

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer