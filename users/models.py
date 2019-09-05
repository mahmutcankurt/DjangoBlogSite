from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=150, null=True)
    postal_code_4 = models.PositiveIntegerField(null=True)
    postal_code_3 = models.PositiveIntegerField(null=True)
    locatity = models.CharField(max_length=30, null=True)
    child_amount = models.PositiveSmallIntegerField(null=True)
    is_merchant = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created(Profile, 'profile'):
            Profile.objects.create(user=instance)
            for user in User.objects.all():
                Profile.objects.get_or_create(user=user)
        instance.Profile.save(attrs={**kwargs})
