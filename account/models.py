from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
	realname = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField()


	def __str__(self):
		return self.realname
	



class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    
admin.site.register(User,UserAdmin)