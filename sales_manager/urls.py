from django.urls import path
from sales_manager import views


urlpatterns = [
    path("book_detail/<int:book_id>/", views.book_detail, name="book-detail"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('book_like/<int:book_id>/<str:redirect_url>/', views.book_like, name='book-like'),
    path("", views.main_page, name='main_page'),
    path('add_comment/<int:book_id>', views.add_comment, name='add_comment')
]