from django.shortcuts import render
from django.urls import reverse
from news.models import New, Category
from django.shortcuts import get_object_or_404

def news_list_view(request):
    
    news = New.objects.all()
    categories = Category.objects.all()
    
    context = {
        'lates_news': news,
        'categories': categories,
        'show_add_button': True
    }
    return render(request, 'index.html', context=context)

def news_detail_view(request, pk):
    news = get_object_or_404(New, id=pk)
    context = {
        'news': news,
        'show_add_button': True
    }
    return render(request, 'news_detail.html', context)

def add_news_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        
        category = get_object_or_404(Category, id=category_id)
        
        news = New.objects.create(title=title, content=content, category=category, image=request.FILES.get('image'))
        return render(request, 'news_detail.html', {'news': news})
    
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'add_news.html', context=context)

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news = New.objects.filter(Category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'lates_news': news,
        'categories': categories,
        'show_add_button': True
    }
    return render(request, 'index.html', context)