from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.

class Role(models.Model):
    ADMIN = 'ADMIN', 'Admin'
    MANAGER = 'MANAGER', 'Manager'
    ENGINEER = 'ENGINEER', 'Engineer'
    STAFF = 'STAFF', 'Staff'
    # CUSTOMER = 'CUSTOMER', 'Customer'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, role=Role.STAFF, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)

        if role not in [Role.STAFF]:
            role = Role.STAFF

        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', Role.ADMIN)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    role=models.CharField(max_length=20, choices=Role.choices, default=Role.STAFF)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [] # this will be email and password only, nothing else is required

    def __str__(self):
        return f"{self.email} ({self.role})"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField('profile_pictures/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "profile of {self.user.email}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
