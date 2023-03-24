from django.contrib import admin

# Register your models here.
from main.models import Idea

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'author')

admin.site.register(Idea, IdeaAdmin)