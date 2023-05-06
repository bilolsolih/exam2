from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel
from . import choices
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), region="UZ", unique=True)
    back_up = PhoneNumberField(blank=True, null=True)

    first_name = models.CharField(verbose_name=_("First name"), max_length=124)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=124)
    profile_photo = models.ImageField(
        verbose_name=_("Profile photo"),
        upload_to="images/accounts/profile/%Y/%m/%d/",
        blank=True, null=True
    )
    gender = models.CharField(verbose_name=_("Gender"), choices=choices.GENDER, max_length=1, default="m")

    is_staff = models.BooleanField(verbose_name=_("Is staff?"), default=False)
    is_active = models.BooleanField(verbose_name=_("Is active?"), default=True)
    is_superuser = models.BooleanField(verbose_name=_("Is superuser?"), default=False)

    is_deleted = models.BooleanField(verbose_name=_('Is user deleted?'), default=False)
    deleted_at = models.DateTimeField(verbose_name=_('The user was deleted at:'), default=timezone.now)

    groups = models.ManyToManyField(verbose_name=_("Groups"), to="auth.Group", related_name="users", blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    # bought_products

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def save(self, *args, **kwargs):
        self.back_up = self.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.phone_number)
