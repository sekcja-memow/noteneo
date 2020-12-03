import datetime
import os
import uuid

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created

from emails.emails import ResetPasswordEmail
from users import managers


def get_file_path(instance, filename: str) -> str:
    today = datetime.date.today().strftime("%Y-%m-%d")
    return os.path.join(settings.UPLOAD_FILES_DIR, today, str(uuid.uuid4()) + filename)


class User(auth_models.AbstractUser):
    """
    from Notes
    bookmarks       - Many2Many with Note
    likes           - Many2Many with Note
    subscription    - One2One with Subscription
    """
    username = None

    email = models.EmailField(unique=True, verbose_name=_('Email address'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(verbose_name=_('Date joined'), default=timezone.now)
    image = models.ImageField(upload_to=get_file_path, default=settings.DEFAULT_USER_IMAGE)

    postal_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=2, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    objects = managers.CustomUserManager()

    class Meta:
        ordering = ('email',)

    def __str__(self):
        return self.email


class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField('users.User', on_delete=models.PROTECT, related_name='subscription')
    start_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('start_date', 'user',)

    @property
    def is_active(self) -> bool:
        return self.start_date + datetime.timedelta(days=31) - timezone.now() < datetime.timedelta(days=0)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    ResetPasswordEmail("noreply@somehost.local",
                       reset_password_token.user,
                       reset_password_token.key).send([reset_password_token.user.email])
