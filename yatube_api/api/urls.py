from rest_framework.routers import DefaultRouter
from django.urls import include, path

from api.views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet

v1_router = DefaultRouter()

v1_router.register(r'posts', PostViewSet, basename='post')
v1_router.register(r'groups', GroupViewSet, basename='group')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')
v1_router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
