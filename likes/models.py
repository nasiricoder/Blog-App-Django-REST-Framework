from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


class LikedItem(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = ("LikedItem")
        verbose_name_plural = ("LikedItems")
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("LikedItem_detail", kwargs={"pk": self.pk})
