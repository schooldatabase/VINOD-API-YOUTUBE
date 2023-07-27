from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoMetadataViewSet(viewsets.ModelViewSet):
    queryset = VideoMetadata.objects.all()
    serializer_class = VideoMetadataSerializer

class VideoCommentViewSet(viewsets.ModelViewSet):
    queryset = VideoComment.objects.all()
    serializer_class = VideoCommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class DislikeViewSet(viewsets.ModelViewSet):
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class UserVideoInteractionMetricsViewSet(viewsets.ModelViewSet):
    queryset = UserVideoInteractionMetrics.objects.all()
    serializer_class = UserVideoInteractionMetricsSerializer

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class TrendingVideoViewSet(viewsets.ModelViewSet):
    queryset = TrendingVideo.objects.all()
    serializer_class = TrendingVideoSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
