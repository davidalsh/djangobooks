from django.urls import path
from manager.views import MyPage, AddLike, AddCommentLike

# hello/
urlpatterns = [
    path("add_like/<int:id>", AddLike.as_view(), name='add-like'),
    path("add_com_like/<int:id>", AddCommentLike.as_view(), name='add-com-like'),
    path("", MyPage.as_view(), name="the-main-page"),
]
