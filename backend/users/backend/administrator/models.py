from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseAbstractUser, BasePermission, BaseGroup, BasePermissionMixin
from common.models import Country
from developer.models import DeveloperPermission, DeveloperGroup


class AdminPermission(BasePermission):
    class Meta(BasePermission.Meta):
        db_table = "admin_permission"
        verbose_name = _("admin_permission")
        verbose_name_plural = _("admin_permissions")


class AdminPermissionMixin(BasePermissionMixin):
    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True

        queryset = self.user_permissions.filter(codename=perm) | AdminPermission.objects.filter(
            admingroup__admin=self, codename=perm
        )
        return queryset.exists()

    def get_all_permissions(self, obj=None):
        return self.user_permissions.all() | AdminPermission.objects.filter(admingroup__admin=self)

    class Meta:
        abstract = True


class AdminGroup(BaseGroup):
    permission = models.ManyToManyField(
        AdminPermission,
        verbose_name=_("permission"),
        blank=True,
        related_name='admingroup_set',
        related_query_name='admingroup',
    )

    class Meta(BaseGroup.Meta):
        db_table = "admin_group"
        verbose_name = _("admin group")
        verbose_name_plural = _("admin groups")


class AdminManager(UserManager):
    def _create_admin_user(self, username, email, phone, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        username = Admin.normalize_username(username)
        user = Admin(username=username, email=email, phone=phone, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, phone=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_admin_user(username, email, phone, password, **extra_fields)

    def create_user(self, username, email=None, password=None, phone=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_admin_user(username, email, phone, password, **extra_fields)


class Admin(BaseAbstractUser, AdminPermissionMixin):
    avatar = models.ImageField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    country = models.ForeignKey(
        Country,
        verbose_name=_('admin country'),
        on_delete=models.SET_NULL,
        null=True,
    )
    groups = models.ManyToManyField(
        AdminGroup,
        verbose_name=_("admin_groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="admin_set",
        related_query_name="admin",
    )
    user_permissions = models.ManyToManyField(
        AdminPermission,
        verbose_name=_("admin permissions"),
        blank=True,
        help_text=_("Specific permissions for this admin."),
        related_name="admin_set",
        related_query_name="admin",
    )

    developer_groups = models.ManyToManyField(
        DeveloperGroup,
        verbose_name=_("Developer group for admin"),
        blank=True,
        related_name="admin_set",
        related_query_name="admin",
    )

    developer_permissions = models.ManyToManyField(
        DeveloperPermission,
        verbose_name=_("developer permissions"),
        blank=True,
        help_text=_("Specific developer permissions for admin"),
        related_name="admin_set",
        related_query_name="admin",
    )

    objects = AdminManager()

    class Meta:
        db_table = "admin"