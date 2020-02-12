from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from service.utils import unique_username_generator
from django.db.models.signals import pre_save
from django.core.validators import RegexValidator
USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class UserManager(BaseUserManager):
    def create_user(self,username,email,phone_no, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("Users must have an user address")

        if not password:
            raise ValueError("Users must have a password")

        if not phone_no:
            raise ValueError("Users must have phone no")

        if not email:
            raise ValueError("Users emaild")

        user_obj = self.model(
            username = username,
            email=self.normalize_email(email),
            full_name=full_name,
            phone_no=phone_no
        )
        user_obj.set_password(password) # change user password
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,username, email,phone_no, full_name=None, password=None):
        user = self.create_user(
                username,
                email,
                phone_no,
                full_name = full_name,
                password=password,
                is_staff=True
        )
        return user

    def create_superuser(self,username, email,phone_no, full_name=None, password=None):
        user = self.create_user(
                username,
                email,
                phone_no,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=300,
        validators=[
            RegexValidator(regex=USERNAME_REGEX,
                           message='Username must be alphanumeric or contain numbers',
                           code='invalid_username'
                           )],
        unique=False,blank=True
    )
    email = models.EmailField(max_length=255, unique=True)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=10, blank=False, unique=True) # validators should be a list
    full_name = models.CharField(max_length=255, blank=True, null=True)
    verified = models.BooleanField(default=False)
    worker=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)# can login
    is_staff = models.BooleanField(default=False) # staff user non superuser
    is_admin = models.BooleanField(default=False) # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['username','phone_no']
    #['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
'''
    @property
    def is_staff(self):
        return self.is_staff

    @property
    def is_admin(self):
        return self.is_admin

    @property
    def is_active(self):
        return self.is_active

'''

def user_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.username:
        # instance.username= unique_username_generator(instance)
         instance.username= instance.full_name


pre_save.connect(user_pre_save_receiver,sender=User)


class GuestEmail(models.Model):
    email = models.EmailField()
    active   = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email