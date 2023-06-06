from rest_framework import serializers
from .models import menu, booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class SingleMenuItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=menu.objects.all())
    class Meta:
        model = menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'

