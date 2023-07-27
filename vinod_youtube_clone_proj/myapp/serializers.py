from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .validations import *
# from .models import UserSubscription, Notification, TrendingVideo, Report

class VideoSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField(validators=[validate_video])
    thumbnail = serializers.FileField(validators=[validate_image])
    class Meta:
        model = Video
        fields = '__all__'

class VideoMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMetadata
        fields = '__all__'

class VideoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoComment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class UserVideoInteractionMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVideoInteractionMetrics
        fields = '__all__'

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class TrendingVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingVideo
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
