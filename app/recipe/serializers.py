from core.models import Recipe
from rest_framework import serializers



class RecipeSerializer(serializers.ModelSerializer):
    # Make user read-only
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'description', 'time_minutes', 'price', 'link']