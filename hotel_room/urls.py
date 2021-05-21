from django.urls import path
from hotel_room import views

urlpatterns = [
    path('', views.room_list, name='main-page'),
    path('room_detail/<int:room_id>/', views.room_detail, name='room-detail'),
]