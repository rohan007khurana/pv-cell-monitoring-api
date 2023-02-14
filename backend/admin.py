from django.contrib import admin
from .models import Reading

# Register your models here.
@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    pass