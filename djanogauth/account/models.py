from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Custom user model
class UserManager(BaseUserManager):
    def create_user(self, email, mobile, userName, password=None, password2=None):
        """
        Creates and saves a User with the given email, mobile, userName and password.
        """
        if not email and not mobile:
            raise ValueError("Users must have an email address and mobile")

        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            userName=userName,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, userName='', password=None):
        """
        Creates and saves a superuser with the given email, mobile, userName and password.
        """
        user = self.create_user(
            email,
            password=password,
            mobile=mobile,
            userName=userName,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    mobile = models.IntegerField(unique=True)
    userName = models.CharField(max_length=100)
    # password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile", "password"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
