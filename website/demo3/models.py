import uuid

from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save


# Create your models here.
class UuidModel(models.Model):
    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


class Person(UuidModel):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    postal_code = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return " ".join((self.first_name, self.last_name))


class Profile(UuidModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="demo3_profile",
    )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    """create a profile when a user is created"""
    if created:
        Profile.objects.create(user=instance)


class TestMe(models.Model):
    identifier = models.CharField(max_length=2000)
    name = models.CharField(max_length=2000)
    source = models.CharField(max_length=2000)
