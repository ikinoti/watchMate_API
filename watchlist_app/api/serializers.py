from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_date):
        instance.name = validated_date.get('name', instance.name)
        instance.description = validated_date.get('description', instance.description)
        instance.active = validated_date.get('active', instance.active)
        instance.save()
        return instance