from django.urls import include,path
from rest_framework import routers
from posts import views

router=routers.DefaultRouter()
router.register(r'posts',views.PostView,"posts")
router.register(r'recipe-posts',views.RecipePostView,"recipe-posts")
router.register(r'recipe-reposts',views.RecipeRepostView,"recipe-reposts")
router.register(r'recipe-comments',views.RecipeCommentView,"recipe-comments")
router.register(r'ingredients-quantities',views.Ingredient_QuantityView,"ingredients-quantities")
router.register(r'ingredients', views.IngredientView,"ingredients")
router.register(r'quantities',views.QuantityView,"quantities")
router.register(r'preparation-steps',views.PreparationStepView,"preparationSteps")

urlpatterns=[
    path("api/",include(router.urls))
]

