from django.contrib import admin
from .models import Task

# Register your models here.

class TO_DOAdmin(admin.ModelAdmin):
  list_display = ("task", "created_at", "due_date",'status','priority','category')

admin.site.register(Task, TO_DOAdmin)
