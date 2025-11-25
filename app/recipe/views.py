
from django.shortcuts import render
from rest_framework import viewsets

from core.models import Recipe
from . serializers import RecipeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . permissions import UpdateOwnRecipe





class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnRecipe, IsAuthenticated]


    def perform_create(self, serializer):
        """Sets the user to logged in user"""
        serializer.save(user = self.request.user)
