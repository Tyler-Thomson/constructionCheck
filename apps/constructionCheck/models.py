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
        user.is_superuser = True
        user.save(using=self._db)
        return user
    # def validate_reg(self, form_data):
    #     errors = []
    #     if len(form_data['first_name']) < 2:
    #         errors.append("First name must contain at least two characters")
    #     if len(form_data['last_name']) < 2:
    #         errors.append("Last name must contain at least two characters")
    #     if len(form_data['email']) == 0:
    #         errors.append("Must submit a valid email")
    #     if len(form_data['password']) < 8:
    #         errors.append("Password must contain at least eight characters")
    #     if form_data['password'] != form_data['password_confirm']:
    #         errors.append("Password does not match password confirmation")
    #     print "Inside the validate method"
    #     return errors
    #
    # def validate_login(self, form_data):
    #     errors = []
    #     if len(form_data['email']) == 0:
    #         errors.append("Must submit a valid email")
    #     if len(form_data['password']) < 8:
    #         errors.append("Password must contain at least eight characters")
    #     return errors

    # def authenticate(self, form_data):
    #     errors = self.validate_login(form_data)
    #
    #     if not errors:
    #         user = User.objects.filter(email = form_data['email']).first() #check to make sure email exists in database
    #         if user: #if the email exists, check the password
    #             if str(form_data['password']) == user.password:
    #                 return user
    #
    #         errors.append('Invalid email/password')
        # return errors

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

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.first_name

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
        string_output = " ID: {} Name: {}"
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
        self.checklist,
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
