from django.contrib.auth.models import User
from .models import UserProfile

def create_user(*args, **kwargs):
    """
    Creates new user
    """
    return User.objects.create_user(*args, **kwargs)

def create_user_profile(*args, **kwargs):
    """
    Creates new user profile
    """
    return UserProfile.objects.create(*args, **kwargs)

def get_user(*args, **kwargs):
    """
    Gets a django user
    """
    return User.objects.get(*args,**kwargs)