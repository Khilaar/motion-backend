import random

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


def code_generator(length=5):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for _ in range(length))


class RegistrationProfile(models.Model):
    code = models.CharField(max_length=5, default=code_generator)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_registration_profile_automatically(sender, instance, created, **kwargs):
    if created:
        RegistrationProfile.objects.create(user=instance)
