from django.db.models import Prefetch, Count, Avg

from sales_manager.models import Comment, Book

def Make_qs():
    comment_query = Comment.objects.all().select_related('user').annotate(count_likes=Count('like'))
    comment_prefetch = Prefetch('comments', queryset=comment_query)
    query_set = Book.objects.all().select_related('author'). \
        prefetch_related(comment_prefetch).annotate(rate_avg=Avg('rated_user__rate'))
    return query_set