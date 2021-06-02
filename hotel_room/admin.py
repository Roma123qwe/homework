from django.contrib import admin
from hotel_room.models import Room, Reserv, Owners, Messages


class HotelAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Room)
admin.site.register(Messages)
admin.site.register(Reserv)
admin.site.register(Owners)
