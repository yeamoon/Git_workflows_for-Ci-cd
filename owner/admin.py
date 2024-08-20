from django.contrib import admin

from .models import Productowner

class Productadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
   

admin.site.register(Productowner, Productadmin)