from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def purchase_post_save(sender, instance, created, **kwargs):
    print("----------Send-mail-signal------")