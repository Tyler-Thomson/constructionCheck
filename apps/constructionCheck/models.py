from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
        if not email:
            raise ValueError('Email address must be valid')
        if not password:
            raise ValueError('Password must be valid')
        if not first_name:
            raise ValueError('First name must be valid')
        if not last_name:
            raise ValueError('Last name must be valid')

        user = self.model(
        first_name = first_name,
        last_name = last_name,
        email = self.normalize_email(email),
        password = password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, password, first_name, last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique = True)
    password = models.CharField(max_length=45)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    #Email is the identifying field
    USERNAME_FIELD = 'email'

    #Want to require these field at registration
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.first_name

    #Does the user have a specific permission?
    # Simplest possible answer: Yes, always
    def has_perms(self, perm, obj=None):
        return True

    #Does the user have permissions to view the app `app_label`?
    # Simplest possible answer: Yes, always
    def has_module_perms(self, app_label):
        return True

    #Is the user a member of staff?
    # Simplest possible answer: All admins are staff
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        string_output = " ID: {} Email: {} Password: {} Active: {} Admin: {}"
        return string_output.format(
        self.id,
        self.email,
        self.password,
        self.is_active,
        self.is_admin,
        )

class Section(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = " Name: {}"
        return string_output.format(
        self.id,
        self.name,
    )

class Checklist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class House(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "houses")
    checklist = models.OneToOneField(Checklist, related_name = "house")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = " ID: {} Address: {} City: {} User: {}"
        return string_output.format(
        self.id,
        self.address,
        self.city,
        self.user,
    )

class Check(models.Model):
    title = models.CharField(max_length=45)
    checklist = models.ForeignKey(Checklist, related_name = "checks")
    section = models.ForeignKey(Section, related_name = "checks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        string_output = " ID: {} Item: {}"
        return string_output.format(
        self.id,
        self.title,
        self.checklist,
        self.section,
    )
