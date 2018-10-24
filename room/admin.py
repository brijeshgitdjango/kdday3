from django.contrib import admin

# Register your models here.
from .models import Floor, Room, Bed

admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Bed)
