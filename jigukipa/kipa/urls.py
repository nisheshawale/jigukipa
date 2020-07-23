from rest_framework import routers
from django.urls import path, include
from .api import RegisterAPI    #, UserAPI
from .api import UserProfileViewset, PostViewset


router = routers.DefaultRouter()
router.register('api/profile', UserProfileViewset)
router.register('api/post', PostViewset)

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('', include(router.urls)),
    # path('api/profile/', UserAPI.as_view(), name='profile'),
]