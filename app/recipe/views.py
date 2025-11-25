
from django.shortcuts import render
from rest_framework import viewsets, mixins

from core.models import Recipe, Tag, Ingredient
from . serializers import RecipeSerializer, TagSerializer, IngredientSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . permissions import UpdateOwnRecipe, UpdateOwnTag, UpdateOwnIngredient





class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnRecipe, IsAuthenticated]


    def get_serializer_class(self):
        if self.action == 'list':
            return RecipeSerializer
        
        return self.serializer_class


    def perform_create(self, serializer):
        """Sets the user to logged in user"""
        serializer.save(user = self.request.user)



class TagViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnTag, IsAuthenticated]



class IngredientViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnIngredient, IsAuthenticated]