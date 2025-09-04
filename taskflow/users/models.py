from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a user with an email and password."""
        if not email:
            raise ValueError("The Email field is required")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)  # Ensure active by default

        user = self.model(email=email, **extra_fields)

        if password:
            user.set_password(password)
        else:
            raise ValueError("The Password field is required for users")

        user.save(using=self._db)
        return user

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Department(models.IntegerChoices):
    HR = 1, "Recursos Humanos"
    IT = 2, "Tecnología"
    SALES = 3, "Ventas"
    MARKETING = 4, "Marketing"
    FINANCE = 5, "Finanzas"
    OPERATIONS = 6, "Operaciones"


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model using email instead of username."""

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    department = models.IntegerField(choices=Department.choices)
    is_boss = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "department",
    ]

    def delete(self, using=None, keep_parents=None):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.email
