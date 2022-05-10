from django.contrib import admin
from .models import post1

# Register your models here.

@admin.register(post1)

class mithu(admin.ModelAdmin):
    abd = ['id', 'title', 'desc']