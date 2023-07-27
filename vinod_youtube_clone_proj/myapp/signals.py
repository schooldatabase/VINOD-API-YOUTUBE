from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Video)
def create_video_metadata(sender, instance, created, **kwargs):
    if created:
        VideoMetadata.objects.create(video=instance, tags="")

@receiver(post_save, sender=VideoComment)
def update_user_interaction_metrics(sender, instance, created, **kwargs):
    if created:
        user_interaction, _ = UserVideoInteractionMetrics.objects.get_or_create(user=instance.user, video=instance.video)
        user_interaction.comments += 1
        user_interaction.save()
