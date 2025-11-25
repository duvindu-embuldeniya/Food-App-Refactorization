from core.models import Recipe, Tag
from rest_framework import serializers



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']



class RecipeSerializer(serializers.ModelSerializer):
    # Make user read-only
    user = serializers.StringRelatedField(read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'description', 'time_minutes', 'price', 'link', 'tags']



    def _get_or_create_tags(self, tags, recipe):
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag
            )
            recipe.tags.add(tag_obj)
    


    def create(self, validated_data):
        """Create a recipe."""

        tags = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        return recipe


    def update(self, instance, validated_data):
        """Update recipe."""

        tags = validated_data.pop('tags', None)

        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)
        

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance





