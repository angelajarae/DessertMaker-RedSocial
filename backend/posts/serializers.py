from rest_framework import serializers
from posts import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        likes_count = serializers.IntegerField(source='likes_count', read_only=True)
        saves_count = serializers.IntegerField(source='saves_count', read_only=True)

        model=models.Post
        fields=["id","user","likes_count","saves_count"]

class RecipePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.RecipePost
        fields="__all__"

class RecipeRepostSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.RecipeRepost
        fields="__all__"

class RecipeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.RecipeComment
        fields="__all__"

class Ingredient_QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Ingredient_Quantity
        fields="__all__"

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Ingredient
        fields="__all__"

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Quantity
        fields="__all__"

class PreparationStepSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PreparationStep
        fields="__all__"
    