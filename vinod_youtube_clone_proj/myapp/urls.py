from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'video-metadata', VideoMetadataViewSet)
router.register(r'video-comments', VideoCommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'dislikes', DislikeViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'interaction-metrics', UserVideoInteractionMetricsViewSet)
router.register(r'subscriptions', UserSubscriptionViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'trending-videos', TrendingVideoViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
