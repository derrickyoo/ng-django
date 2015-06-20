from django.contrib.auth.models import AbstractBaseUser
from django.db import models


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
