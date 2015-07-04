from django.contrib import admin
from .models import MyUser, Comments, Posts

admin.site.register(MyUser)
admin.site.register(Comments)
admin.site.register(Posts)
