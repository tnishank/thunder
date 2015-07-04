from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	location = models.CharField(max_length=100)
	about_me = models.TextField("about me")
	member_since = models.DateField("member since",auto_now_add=True)

	def __str__(self):
		return self.user.username

	@property
	def data(self):
		return UserProfileSerializer(self).data

# INFO: avoid circular import
from .serializers import UserProfileSerializer