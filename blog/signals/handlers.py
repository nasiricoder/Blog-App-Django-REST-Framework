from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .. import models


@receiver(signal=post_save, sender=settings.AUTH_USER_MODEL)
def create_Author_for_new_user(sender, **kwargs):
    if kwargs['created']:
        models.Author.objects.create(user=kwargs['instance'])
