from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from users import managers


class User(auth_models.AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name=_('Email address'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    address = models.CharField(max_length=200, blank=True, verbose_name=_('Address'))

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(verbose_name=_('Date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    objects = managers.CustomUserManager()

    class Meta:
        ordering = ('email',)

    def __str__(self):
        return self.email
