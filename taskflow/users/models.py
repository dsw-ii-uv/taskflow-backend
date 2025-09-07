from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser debe tener is_superuser=True.")
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser debe tener is_staff=True.")

        return self.create_user(email, password, **extra_fields)


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
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "department",
    ]

    objects = UserManager()

    def __str__(self):
        return self.email
