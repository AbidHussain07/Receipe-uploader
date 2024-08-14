from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ['receipe_name' , 'user' ]