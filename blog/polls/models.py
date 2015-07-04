from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
	user = models.OneToOneField(User)
	location = models.CharField(max_length=100)
	about_me = models.TextField("about me")
	member_since = models.DateField("member since",auto_now_add=True)

	class Meta:
		db_table = "myuser"

	def __str__(self):
		return self.user.username
		
class Comments(models.Model):
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	author_id = models.ForeignKey("MyUser")
	post_id = models.ForeignKey("Posts")

	class Meta:
		db_table = "comments"

class Posts(models.Model):
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	author_id = models.ForeignKey("MyUser")

	class Meta:
		db_table = "posts"