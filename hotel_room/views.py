from datetime import date, timedelta
from django.contrib.auth import authenticate, login, logout
from django.db.models import Avg, Count
from django.shortcuts import render, redirect
from django.views import View
from hotel_room.models import Room, Reserv, Owners, Rating


class LoginView(View):
    def get(self, request):
        return render(request, 'hotel_room/login.html')

    def post(self, request):
        user = authenticate(username=request.POST['login'], password=request.POST['pwd'])
        if user is not None:
            login(request, user)
            return redirect('main-page')
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('main-page')

def room_list(request):
    room = Room.objects.all()
    context = {'rooms': room}
    return render(request, 'hotel_room/main_page.html', context=context)

def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    context = {'room': room}
    return render(request, 'hotel_room/room_detail.html', context=context)


def room_reservation(request, room_id):
    if request.user.username == '':
        return redirect('login')
    today = date.today()
    room = Room.objects.get(id=room_id)
    yesterday = date.today() + timedelta(days=1)
    reservs = Reserv.objects.filter(what_room_id=room_id)
    context = {'room': room, 'exept': False, 'today': today,'yesterday': yesterday}
    if len(request.POST) != 0:
        for reserv in reservs:
            if reserv.reservation_from <= date.fromisoformat(request.POST['reserv_from']) \
                    and date.fromisoformat(request.POST['reserv_from']) <= reserv.reservation_to:
                context = {'room': room, 'exept': True, 'today': today,'yesterday': yesterday}
                return render(request, 'hotel_room/room_reservation.html', context=context)
        Reserv.objects.create(reservation_from=request.POST['reserv_from'], reservation_to=request.POST['reserv_to'],\
                           what_room_id=room_id, who_reserv_id=request.user.id )
        return redirect('/hotel/')
    return render(request, 'hotel_room/room_reservation.html', context=context)


def add_owners(request, room_id):
    for owner in Owners.objects.filter(room_id=room_id):
        if owner.add_to <= date.today():
            owner.delete()
    today = date.today()
    room = Room.objects.get(id=room_id)
    context = {'room': room, 'today': today, 'exept': False}
    if request.user.username == '':
        return redirect('login')
    if len(request.POST) != 0:
        if len(Owners.objects.filter(room_id=room_id)) == Room.objects.get(id=room_id).places_in_room:
            context = {'room': room, 'today': today, 'exept': True}
            return render(request, 'hotel_room/owner_add.html', context=context)
        Owners.objects.create(name=request.POST['owners_name'], room_id=room_id, add_to=request.POST['add_to'])
        return render(request, 'hotel_room/owner_add.html', context=context)
    return render(request, 'hotel_room/owner_add.html', context=context)


def rating(request):
    if len(request.POST) != 0:
        Rating.objects.create(eat=request.POST['eat'], service=request.POST['service'], \
                              entertainment=request.POST['entertaiment'],\
                              cleanness=request.POST['cleanness'], personal=request.POST['personal'])
    return render(request, 'hotel_room/rating.html')

def rating_stat(request):
    ratings = Rating.objects.aggregate(avg_eat=Avg('eat')).aggregate(avg_service=Avg('service')).\
        aggregate(avg_entertainment=Avg('entertainment')).aggregate(avg_personal=Avg('personal')).\
        aggregate(avg_cleanness=Avg('cleanness')).aggregate(Count_eat=Count('eat'))
    context= {'ratings': ratings}
    return render(request, 'hotel_room/rating_stat.html', context=context)