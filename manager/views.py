from django.db.models import Count, Prefetch
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from manager.models import Book, LikeBookUser, LikeCommentUser, Comment


class MyPage(View):
    def get(self, request):
        context = dict()
        comment_query = Comment.objects.annotate(count_like=Count("users_like"))
        comments = Prefetch("comments", comment_query)
        context['books'] = Book.objects.prefetch_related("authors", comments). \
            annotate(count_like=Count("users_like"))
        return render(request, "index.html", context)


class AddLike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            LikeBookUser.objects.create(user=request.user, book_id=id)
        return redirect("the-main-page")


class AddCommentLike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id)
        return redirect("the-main-page")
