from rest_framework import serializers
from main.models import Event, Category
from app_user.serializers import AppUserDetailsSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('slug',)


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventALLSerializer(serializers.ModelSerializer):
    author = AppUserDetailsSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'image',
            'date',
            'venue',
            'slug',
            'category',
            'author',
            'featured',
            'event_url',
            'community'
        ]
