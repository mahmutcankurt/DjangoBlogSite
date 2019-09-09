from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=150, null=True)
    address_2 = models.CharField(max_length=150, null=True)
    postal_code_3 = models.PositiveIntegerField(null=True)
    locatity = models.CharField(max_length=30, null=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
