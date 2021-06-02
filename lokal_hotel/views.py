from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from hotel_room.models import Owners, Room, Messages


class LoginView(View):
    def get(self, request):
        return render(request, 'lokal_hotel/login_admin.html')

    def post(self, request):
        user = authenticate(username=request.POST['login'], password=request.POST['pwd'])
        if user is not None:
            login(request, user)
            return redirect('main-page-admin/')
        return redirect('login_admin')

def login_lokal(request):
    context = {'room_id': request.GET['room_id'], 'user': request.GET['name']}
    if len(request.GET) != 0:
        owners = Owners.objects.filter(room_id=request.GET['room_id'])
        if request.GET['name'] in owners:
            return redirect(f'main_page/{context["room_id"]}/{context["user"]}/')
    return render(request, 'login.html')

def main_page(request, room_id, name):
    messages = Messages.objects.filter(user=name)
    context = {'messages': messages}
    if request.POST != '':
        Messages.objects.create(user=name, text=request.POST['text'])
    return render(request, 'lokal_hotel/main_page.html', context=context)




