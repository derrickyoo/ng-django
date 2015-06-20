from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):

    """Manager class required when substituding User model."""

    def create_user(self, email, password=None, **kwargs):
        """Create user."""
        # Email is required
        if not email:
            raise ValueError('Users must have a valid email address.')

        # Username is required
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        # Define model attribote on the Account Manager class
        # self.model refers to the model attribut of BaseUserManager
        # Defaults to settings.AUTH_USER_MODEL, which needs to be changed
        # to point to the Account class in the settings.py file
        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_super_user(self, email, password, **kwargs):
        """Create super user."""
        # Use create_user to handle account creation
        account = self.create_user(email, password, **kwargs)

        # Use create_super_user to handle turning Account into a superuser.
        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):

    """Using AbstractBaseUser to extend Account beyond User."""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    tagline = models.CharField(max_length=140, blank=True)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # <modal name>Manager convention
    objects = AccountManager()

    # Django's built-in User requires a username
    # Treat unique email field as the username for this model
    USERNAME_FIELD = 'email'

    # This model is replacing the User model using AbstractBaseUser
    # Django requires us to sepcify required fields in this way.
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        """String representation of an account with the email.

        Example: <Account: email>
        """
        return self.email

    def get_full_name(self):
        """Django convention and good practice to return full name."""
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        """Django convention and good practice to return short name."""
        return self.first_name
