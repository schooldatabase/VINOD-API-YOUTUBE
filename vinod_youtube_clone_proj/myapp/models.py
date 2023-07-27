from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True)  # Store the video thumbnail
  
    def __str__(self):
        return self.title

    
class VideoMetadata(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.video.title} - Metadata"

class VideoComment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} commented on {self.video.title}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} liked {self.video.title}"

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    disliked_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} disliked {self.video.title}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} favorited {self.video.title}"

class UserVideoInteractionMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    favorites = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} - {self.video.title} Interaction Metrics"
    
class UserSubscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    channel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.subscriber.username} subscribed to {self.channel.username}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - Notification"

    
class TrendingVideo(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.video.title} - Trending"

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=100)
    content_id = models.PositiveIntegerField()
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} reported {self.content_type} {self.content_id}"