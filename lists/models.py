from django.db import models
import datetime
#import pytz
from django.utils import timezone
# Create your models here.
class e_mailaddress(models.Model):
	email = models.CharField(max_length = 100)
	#pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.email
	
	#def was_published_recently(self):
			#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	#was_published_recently.admin_order_field = 'pub_date'
	#was_published_recently.boolean = True
	#was_published_recently.short_description = 'Published recently?'
		

