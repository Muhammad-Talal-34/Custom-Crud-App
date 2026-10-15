from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address lazmi hai')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        
        
        user.set_password(password)
        user.save(using=self._db)
        return user

#  Custom Table 
class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    ROLE_CHOICES = (
        ('admin', 'Admin'),       # Manages users
        ('manager', 'Manager'),   # Manages products
        ('user', 'User'),         # Views products only
    )
    
    # 2. Add the role field (defaulting to standard user for safety)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username' #login with
    REQUIRED_FIELDS = ['email'] # Terminal se user banate waqt kya zaroori hai

    def __str__(self):
        return self.username