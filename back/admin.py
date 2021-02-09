from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Message)
admin.site.register(User)
admin.site.register(Tache)

class Message_admin(admin.ModelAdmin):
    list_display = ('prenom','date')
    list_filter = ('prenom', 'date')


admin.site.register(Message,Message_admin)