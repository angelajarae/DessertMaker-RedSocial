from rest_framework import viewsets
from posts import serializers
from posts import models

# Create your views here.
class PostView(viewsets.ModelViewSet):
    serializer_class=serializers.PostSerializer
    queryset=models.Post.objects.all()

class RecipePostView(viewsets.ModelViewSet):
    serializer_class=serializers.RecipePostSerializer
    queryset=models.RecipePost.objects.all()

class RecipeRepostView(viewsets.ModelViewSet):
    serializer_class=serializers.RecipeRepostSerializer
    queryset=models.RecipeRepost.objects.all()

class RecipeCommentView(viewsets.ModelViewSet):
    serializer_class=serializers.RecipeCommentSerializer
    queryset=models.RecipeComment.objects.all()

class Ingredient_QuantityView(viewsets.ModelViewSet):
    serializer_class=serializers.Ingredient_QuantitySerializer
    queryset=models.Ingredient_Quantity.objects.all()

class IngredientView(viewsets.ModelViewSet):
    serializer_class=serializers.IngredientSerializer
    queryset=models.Ingredient.objects.all()

class QuantityView(viewsets.ModelViewSet):
    serializer_class=serializers.QuantitySerializer
    queryset=models.Quantity.objects.all()

class PreparationStepView(viewsets.ModelViewSet):
    serializer_class=serializers.PreparationStepSerializer
    queryset=models.PreparationStep.objects.all()