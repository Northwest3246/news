from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    news = Post.objects.filter(type=news).order_by('-created_at')
    return render(request, 'news_list.html', {'news_list': news})

def news_detail(request, pk):
    news_item = get_object_or_404(Post, pk=pk)
    return render(request, 'news_detail.html', {'news': news_item})
