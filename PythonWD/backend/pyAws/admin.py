from django.contrib import admin
from .models import Card
# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'large')
admin.site.register(Card, CardAdmin)