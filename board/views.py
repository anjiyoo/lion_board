from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm

# 클래스 기반 뷰 버전
class ItemLV(ListView):
    model = Item
    # ListView의 기본 세팅
    # - 보여줄 템플릿 template : 앱이름/모델명(소문자)_list.html
    # - 값 전달 context : object_list
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = 'Tiger'
        return context


# 클래스 기반 뷰 버전
class ItemDV(DetailView):
    model = Item
    # DetailView 기본 세팅
    # - 보여줄 템플릿 template : 앱이름/모델명(소문자)_detail.html
    # - 값 전달 context : object
    # pk를 통해서 대상 데이터 가져옴
    # url에서 pk를 가져오는 내용이 정의되어 있어야 함


# 클래스 기반 뷰 버전
class ItemCV(CreateView):
    model = Item
    success_url = reverse_lazy('index')
    fields = ['title', 'content']
    # - 보여줄 템플릿 template : 앱이름/모델명(소문자)_form.html

# 클래스 기반 뷰 버전
class ItemDeV(DeleteView):
    model = Item
    success_url = reverse_lazy('index')
    # 지울건지 확인 : 앱이름/모델명(소문자)_confirm_delete.html


# 함수형 뷰 버전
def itemLV(request):
    # 모델에서 데이터 가져오기
    object = Item.objects.all()
    name = 'Lion'
    # 값을 context에 담기
    context = {
        'object_list' : object,
        'name' : name
    }
    # 템플릿에 결합
    # 페이지 반환
    return render(request=request, template_name='board/item_list.html', context=context)

# 함수형 뷰 버전
def itemDV(request, pk):  # urls.py에서 pk로 전달받음
    object = Item.objects.get(pk=pk)  # pk 설정 // object_id로 지정할 경우 url도 같이 설정
    context = {
        'object' : object,
    }
    return render(request=request, template_name='board/item_detail.html', context=context)

# 함수형 뷰 버전
def content_comment(request, pk):  # pk : item pk
    # 해당 item pk를 가진 대상에 추가적으로 comment를 저장
    item = Item.objects.get(pk=pk)  # object 가져오기

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # 댓글 내용 저장
            comment = form.save(commit=False)
            # foreignKey 연결
            comment.item = item
            comment.save()
    elif request.method=="GET":
        form = CommentForm()
    return render(request, 'board/item_detail.html', {'object':item, 'form':form})








def test(request):
    return HttpResponse("요청 잘 받았어")

def test1(request, pk):
    return HttpResponse(f"test1 pk: {pk} 이야")


