from django.urls import path
from .views import test, test1, ItemLV, ItemDV, ItemCV, ItemDeV, itemLV, itemDV, content_comment

urlpatterns = [
    path("", ItemLV.as_view(), name='index'),
    # path("detail/<int:pk>/", ItemDV.as_view(), name='detail'),  기존 DetailView
    path("detail/<int:pk>/", content_comment, name='detail'),  # 댓글기능이 들어간 DetailView
    # {% url 'detail' object.id %} -> detail은 이름, object.id는 int:pk
    path("create/", ItemCV.as_view(), name='create'),
    path("delete/<int:pk>/", ItemDeV.as_view(), name='delete'),



    path("f/", itemLV),
    path("f/<int:pk>/", itemDV),
    path("lion/<int:pk>/", test1),
    path("lion/tiger/", test),
]