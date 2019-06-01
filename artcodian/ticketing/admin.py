from django.contrib import admin

# Register your models here.

from .models import Tickets

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id_code', 'pur_date', 'title', 'scene')

admin.site.register(Tickets, TicketsAdmin)
