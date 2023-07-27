from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Video)
admin.site.register(VideoMetadata)
admin.site.register(VideoComment)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Favorite)
admin.site.register(UserVideoInteractionMetrics)
admin.site.register(UserSubscription)
admin.site.register(Notification)
admin.site.register(TrendingVideo)
admin.site.register(Report)
