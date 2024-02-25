from django.contrib import admin
from .models import Post,Ingredient_Quantity, Ingredient, Quantity, PreparationStep,RecipePost,RecipeComment,RecipeRepost

# Register your models here.
admin.site.register(Post)
admin.site.register(RecipePost)
admin.site.register(RecipeComment)
admin.site.register(RecipeRepost)
admin.site.register(Ingredient_Quantity)
admin.site.register(Ingredient)
admin.site.register(Quantity)
admin.site.register(PreparationStep)