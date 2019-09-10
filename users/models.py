from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def upload_to(instance, filename):
    return '%s/%s/%s' % ('profile_photo', instance.user.username, filename)


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNDEFINED = 'U'
    GENDER = ((MALE, 'Male'), (FEMALE, 'Female'), (UNDEFINED, 'Undefined'))

    phone_number = models.CharField(max_length=11, verbose_name='Phone Number', blank=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, verbose_name='User')
    gender = models.CharField(max_length=1, default=3, verbose_name='GENDER', choices=GENDER, blank=True)
    birth_date = models.DateField(null=True)
    bio = models.CharField(null=True, max_length=500)
    address = models.CharField(max_length=150, null=True)
    address_2 = models.CharField(max_length=150, null=True)
    postal_code_3 = models.PositiveIntegerField(null=True)
    locatity = models.CharField(max_length=30, null=False)
    profile_photo = models.ImageField(upload_to=upload_to, default='profile_photo/default/user-default.jpg', verbose_name='Profile Photo', blank=False)

    class Meta:
        verbose_name_plural = 'User Informations'

    def get_full_name_or_username(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    def __str__(self):
        return "%s Profile" % (self.get_full_name_or_username())


def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(receiver=create_user_profile, sender=User)
