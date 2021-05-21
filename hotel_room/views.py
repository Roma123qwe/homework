from django.shortcuts import render
from hotel_room.models import Room

def room_list(request):
    room = Room.objects.all()
    context = {'rooms': room}
    return render(request, 'hotel_room/main_page.html', context=context)

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {'room': room}
    return render(request, 'hotel_room/room_detail.html', context=context)

