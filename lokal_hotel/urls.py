from django.urls import path

from lokal_hotel import views

urlpatterns = [
    path('login_admin/', views.LoginView.as_view, name='login_admin'),
    path('login/', views.LoginView.as_view, name='login'),
    path('login/<int:room_id>/<str:name>/', views.main_page, name='main_page'),

]