from django.db import models

class Room(models.Model):
    places_in_room = models.PositiveSmallIntegerField()
    count_per_night = models.PositiveIntegerField()
    is_free = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return 'Room for ' + str(self.places_in_room) +' person'
