from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager para perfiles """
    def create_user(self,email,password=None,first_name=None,last_name=None,gender=None,company=None,city=None,title=None):
        if not email:
            raise ValueError('email unexistent')
        
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name)

        user.save(using = self._db)
        user.set_password(password)
        return user

    def create_superuser(self, email,password=None,first_name=None,last_name=None):
        user = self.create_user(email,password,first_name,last_name)

        user.is_superuser = True

        user.is_staff = True

        
        user.save(using = self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo para usuarios"""
    first_name= models.CharField(max_length=255,blank=True,null=True)
    last_name=models.CharField(max_length=255,blank=True,null=True)
    email= models.EmailField(max_length=255,unique=True)
    gender=models.CharField(max_length=6,blank=True,null=True)
    company=models.CharField(max_length=255,blank=True,null=True)
    city=models.CharField(max_length=255,blank=True,null=True)
    title=models.CharField(max_length=255,blank=True,null=True)
    coord = models.CharField(max_length=255,blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    #REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.first_name if self.first_name else '' +" "+self.last_name if self.last_name else ''