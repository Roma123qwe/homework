from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=100, default='Room')
    places_in_room = models.PositiveSmallIntegerField()
    count_per_night = models.PositiveIntegerField()
    is_free = models.BooleanField(default=True)
    description = models.TextField()


    def __str__(self):
        return self.title

class Reserv(models.Model):
    reservation_from = models.DateField()
    reservation_to = models.DateField()
    who_reserv = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='Reservs',
                                   )
    what_room = models.ForeignKey(Room,
                                  on_delete=models.CASCADE,
                                  related_name='Reservs',
                                  )

class Owners(models.Model):
    name = models.CharField(max_length=50)
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE,
                              related_name='owner')
