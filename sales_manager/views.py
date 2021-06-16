from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from sales_manager.models import Book, Comment, UserRateBook
from django.views import View
from django.db.models import Count, Prefetch, Avg

from sales_manager.utils import Make_qs


def main_page(request):
    query_set = Make_qs()
    context = {"books": query_set}
    return render(request, "sales_manager/index.html", context=context)


def book_detail(request, book_id):
    query_set = Make_qs()
    book = query_set.get(id=book_id)
    context = {"book": book}
    return render(request, "sales_manager/book_detail.html", context=context)

@login_required(login_url='/shop/login/')
def book_like(request, book_id, rate, redirect_url):
    UserRateBook.objects.update_or_create(
        book_id=book_id,
        user=request.user,
        defaults={'rate': rate}
    )
    book = Book.objects.get(book_id=book_id)
    book.avg_rate = book.rated_user.aggregate(rate=Avg('rate'))['rate']
    book.save(update_fields=['avg_rate'])
    if redirect_url == 'main-page':
        return redirect('main_page')
    elif redirect_url == 'book_detail':
        return redirect('book-detail', book_id=book_id)


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

@login_required(login_url='/shop/login/')
@require_http_methods(['POST'])
def add_comment(request, book_id):
    text = request.POST['text']
    Comment.objects.create(text=text,
                           user=request.user,
                           book_id=book_id,
                           )
    return redirect('book-detail', book_id=book_id)

@login_required(login_url='/shop/login/')
def comment_like(request, comment_id):
    com = Comment.objects.get(id=comment_id)
    if request.user in com.like.all():
        com.like.remove(request.user)
    else:
        com.like.add(request.user)
    return redirect('book_detail', book_id=com.book_id)

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer