from django.contrib import admin
# Register your models here.
from lists.models import e_mailaddress
#admin.site.register(e_mailaddress)
#class e_mailaddressInline(admin.StackedInline):
	#model = e_mailaddress
	#extra = 3


class ListsAdmin(admin.ModelAdmin):
	fieldsets = [
		
		(None,          {'fields':['email']}),]

	#inlines = [e_mailaddressInline]
	#list_display = ('email','was_published_recently')
	#list_filter = ['pub_date']
	search_fields = ['email']
	#search_fields = ['pub_date']


admin.site.register(e_mailaddress,ListsAdmin)

#class Person(admin.ModelAdmin):
	#fieldsets = [
		#(None,				{'fields':['real_name']}),
		#(None,				{'fields':['nick_name']}),
		#(None,				{'fields':['accountemail']}),
		#(None,				{'fields':['password1']}),
		#(None,				{'fields':['password2']}),]

	#search_fields = ['real_name']
	#search_fields = ['nick_name']


#admin.site.register(person,Person)