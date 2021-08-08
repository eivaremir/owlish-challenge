from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager para perfiles """
    def create_user(self,email,first_name=None,last_name=None,gender=None,company=None,city=None,title=None):
        if not email:
            raise ValueError('email unexistent')
        
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name)

        user.save(using = self._db)

        return user

    def create_superuser(self, email,first_name=None,last_name=None):
        user = self.create_user(email,first_name,last_name)

        user.is_superuser = True
        user.is_staff = True

        
        user.save(using = self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo para usuarios"""
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email= models.EmailField(max_length=255,unique=True)
    gender=models.CharField(max_length=6)
    company=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    coord = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.first_name+" "+self.last_name