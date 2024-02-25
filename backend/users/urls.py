from django.urls import include,path
from rest_framework import routers
from users import views

router=routers.DefaultRouter()
router.register(r'user-profiles',views.UserProfileView,"user-profiles")
router.register(r'likes',views.LikeView,"likes")
router.register(r'saves',views.SaveView,"saves")
router.register(r'follows',views.FollowerView,"followers")

urlpatterns=[
    path("api/",include(router.urls))
]