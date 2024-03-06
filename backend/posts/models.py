from typing import Any
from django.db import models
from users.models import UserProfile


QUANTITY_MEASURE_CHOICES = [
    ("grams", "Grams"),
    ("units", "Units"),
    ("ounces", "Ounces"),
    ("cups", "Cups"),
    ("pieces", "Pieces"),
    ("liters", "Liters"),
    ("mililiters", "Milliliters"),
    ("tablespoon", "Tablespoon"),
    ("teaspoon", "Teaspoon"),
]


class Post(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    @property
    def likes_count(self):
        return self.like_set.count()
    @property
    def saves_count(self):
        return self.save_set.count()
    
    @property
    def reposts_count(self):
        return RecipeRepost.objects.filter(recipe_post__post_id=self.pk).count()
    
    @property
    def post_type(self):
        if RecipePost.objects.filter(post=self).exists():
            return 'RecipePost'
        elif RecipeRepost.objects.filter(post=self).exists():
            return 'RecipeRepost'
        elif RecipeComment.objects.filter(post=self).exists():
            return 'RecipeComment'
        else:
            return None

    def __str__(self) :
        return f"{self.user.username} {self.pk}"

class RecipePost(models.Model):
    post=models.OneToOneField(Post,on_delete=models.CASCADE)
    name=models.CharField(blank=False,null=False,max_length=50)
    description=models.TextField(blank=True, null=True)
    #image=models.ImageField(blank=True, null=True)
    timestamp=models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.name

class RecipeRepost(models.Model):
    post=models.OneToOneField(Post,on_delete=models.CASCADE)
    text=models.TextField(blank=False,null=False)
    recipe_post=models.ForeignKey(RecipePost,on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.text


class RecipeComment(models.Model):
    post=models.OneToOneField(Post,on_delete=models.CASCADE)
    text=models.TextField(blank=False,null=False)
    recipe_post=models.ForeignKey(RecipePost,on_delete=models.CASCADE)

    def __str__(self) :
        return self.text


class Ingredient(models.Model):
    name=models.CharField(blank=False,max_length=50)

    def __str__(self):
        return self.name

class Quantity(models.Model):
    quantity_number=models.FloatField(blank=False,null=False)
    quantity_measure=models.CharField(max_length=15,blank=False,choices=QUANTITY_MEASURE_CHOICES,default="grams")

    def __str__(self):
        return f"{self.quantity_number} {self.quantity_measure}"

class Ingredient_Quantity(models.Model):
    ingredient=models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    quantity=models.OneToOneField(Quantity, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_post=models.ForeignKey(RecipePost,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} {self.ingredient}"


class PreparationStep(models.Model):
    description=models.TextField(blank=False,null=False)
    step_order=models.IntegerField(blank=False,null=False)
    recipe_post=models.ForeignKey(RecipePost,on_delete=models.CASCADE)

    def __str__(self):
        return self.description



