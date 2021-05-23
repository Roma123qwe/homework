from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from hotel_room.models import Room, Reserv


class LoginView(View):
    def get(self, request):
        return render(request, 'sales_manager/login.html')

    def post(self, request):
        user = authenticate(username=request.POST['login'], password=request.POST['pwd'])
        if user is not None:
            login(request, user)
            return redirect('main_page')
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('main_page')

def room_list(request):
    room = Room.objects.all()
    context = {'rooms': room}
    return render(request, 'hotel_room/main_page.html', context=context)

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {'room': room}
    return render(request, 'hotel_room/room_detail.html', context=context)

def room_reservation(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {'room': room, 'exept': False}
    reservs = Reserv.objects.filter(what_room_id=room_id).all()
    if len(request.POST) != 0:
        if len(Reserv.objects.filter(reservation_from__range=[request.POST['reserv_from'], request.POST['reserv_to']],\
                                 what_room_id=room.id).all()) != 0:
            context = {'room': room, 'exept': True}
            return render(request, 'hotel_room/room_reservation.html', context=context)
        Reserv.objects.create(reservation_from=request.POST['reserv_from'], reservation_to=request.POST['reserv_to'],\
                           what_room_id=room_id, who_reserv_id=request.user.id )
        return redirect('/hotel/')
    return render(request, 'hotel_room/room_reservation.html', context=context)