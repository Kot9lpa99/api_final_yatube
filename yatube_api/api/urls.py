from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from api.views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet

v1_router = DefaultRouter()
jwt_patterns = [
    path('jwt/create/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/',
         TokenVerifyView.as_view(), name='token_verify'),
]

v1_router.register(r'posts', PostViewSet, basename='post')
v1_router.register(r'groups', GroupViewSet, basename='group')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')
v1_router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include(jwt_patterns)),
]
