from django.db.models.signals import post_save #to save post meth
from django.contrib.auth.models import User
from django.dispatch import receiver #receive the signal
from .models import profile


@receiver(post_save, sender= User)
def build_profile(sender, instance,created, **kwargs):
    if created:
        profile.objects.create(user = instance)

@receiver(post_save, sender= User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()