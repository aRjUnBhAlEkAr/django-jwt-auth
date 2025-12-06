# default django imports
from django.db import models

# required django imports
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

# BaseUserManager:
# -> Provides helper methods for creating users and superusers.
# -> Makes it easier to define your own user model with custom fields (like email instead of username).
# -> Ensures Django admin and createsuperuser command work correctly with your custom user model.
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address.")
        
        email = self.normalize_email(email=email)
        
        user = self.model(
            email=email,
            name=name,
        )
    
        user.set_password(password)
        user.save(using=self._db)
        
    
    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        
        superuser = self.create_user(email=email, name=name, password=password)
        return 
    
    
class User(AbstractBaseUser):
    # user realted models fields
    email = models.EmailField(verbose_name="EMAIL", max_length=255, unique=True)
    name = models.CharField(verbose_name="NAME", max_length=200, blank=False)
    
    # user related role based field
    is_staff = models.BooleanField(default=False)   # staff-level access.
    is_admin = models.BooleanField(default=False)   # full permissions.
    
    # user related status field
    is_active = models.BooleanField(default=True)   # active/inactive user.
    
    # user related created_at and updated_at – auto-managed timestamps.
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    # Unique login identifier
    USERNAME_FIELD = 'email'
    # Fields required when creating superuser
    REQUIRED_FIELDS = ['name']
    
    # objects is the default manager for your model.
    # CustomUserManager() is a manager class that inherits from BaseUserManager and defines methods like create_user and create_superuser.
    # By assigning it to objects, you are telling Django:
    #      “Use this custom manager whenever I do User.objects queries or create users.”
    objects = CustomUserManager()
    
    # return respective users email. you can set value in it as per requirements
    def __str__(self):
        return self.email
    
    def has_perm(self, perm):
        # Purpose: Checks if the user has a specific permission.
        # Parameter: perm → A string like "app_label.permission_codename"
        # Usage: Django uses this method internally to determine whether a user can perform a particular action (like user.has_perm("auth.add_user")).
        
        # Returns True if the user is is_admin.
        # Ignores the perm parameter (so all admin users are treated as having all permissions).
        return self.is_admin
    
    def has_module_perm(self, app):
        # Purpose: Checks if the user has any permissions in a given app/module.
        # Parameter: app_label → Name of the Django app, e.g., "auth" or "students"
        # Usage: Django uses this when displaying admin app lists or determining access at the app/module level.
        
        # Returns True if the user is is_admin.
        # Ignores the actual app label; all admin users are considered to have module-level access.
        return self.is_admin