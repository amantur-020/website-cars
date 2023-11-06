from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, phone_number,password=None,**extra_fields):
        if not phone_number:
            raise ValueError("Введите номер телефона")
        
        user =self.model(phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(phone_number,password,extra_fields)
        



class Users(AbstractBaseUser,PermissionsMixin):
    phone_number=models.CharField(max_length=20,unique=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(null=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD = "phone_namber"
    REQUIRED_FIELDS=[]

    def __str__(self) -> str:
        return self.phone_number
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_users'  # Add this related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_users'  # Add this related_name
    )
    
    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"