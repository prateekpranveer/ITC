from django.shortcuts import render
from .models import Blog, Category

def search(request):
    x = Category.objects.all()

    query = request.GET['query']
    allPosts = Blog.objects.filter(title__icontains = query)
    return render(request, 'search.html', {'allPosts': allPosts, 'x': x, 'query': query})


def home(request):

    x = Category.objects.all()

    skincare = Blog.objects.filter(category_id = 1)[:6]
    haircare = Blog.objects.filter(category_id = 2)[:4]
    DIY = Blog.objects.filter(category_id = 3)[:6]
    sustanibility = Blog.objects.filter(category_id = 4)[:4]
    wellness = Blog.objects.filter(category_id = 5)[:6]
    meditation = Blog.objects.filter(category_id = 7)[:4]
    
    
    allPosts = Blog.objects.order_by("-posted")
    return render(request, 'index.html', {'allPosts': allPosts , 'x': x, 'skincare': skincare, 'haircare': haircare, 'DIY': DIY, 'sustanibility': sustanibility, 'wellness': wellness, 'meditation': meditation})

def single_post(request,slug):
    x = Category.objects.all()
    
    slugpost = Blog.objects.filter(slug=slug)
    recentpost = Blog.objects.all()[:4]
    return render(request, 'single_blog.html', {'slugpost': slugpost, 'recentpost': recentpost, 'x': x})

def category(request, category):
    x = Category.objects.all()
    category = category.lower()
    
    if category == 'skincare':
        allPosts = Blog.objects.filter(category_id = 1)
        cat = Category.objects.filter(slug = category)
        return render(request, 'category.html', {'allPosts': allPosts, 'cat': cat, 'x': x})

    elif category =='haircare':
        allPosts = Blog.objects.filter(category_id = 2)
        cat = Category.objects.filter(slug = category)
        return render(request, 'category.html', {'allPosts': allPosts, 'cat': cat, 'x': x})

    elif category =='diy':
        allPosts = Blog.objects.filter(category_id = 3)
        cat = Category.objects.filter(slug = category)
        return render(request, 'category.html', {'allPosts': allPosts, 'cat': cat, 'x': x})

    elif category =='sustainibility':
        cat = Category.objects.filter(slug = category)
        allPosts = Blog.objects.filter(category_id = 4)
        return render(request, 'category.html', {'allPosts': allPosts, 'cat': cat, 'x': x})

    elif category =='wellness':
        cat = Category.objects.filter(slug = category)
        allPosts = Blog.objects.filter(category_id = 5)
        return render(request, 'category.html', {'allPosts': allPosts, 'cat': cat, 'x': x})

    elif category =='meditation':
        cat = Category.objects.filter(slug = category)
        allPosts = Blog.objects.filter(category_id = 7)
        return render(request, 'category.html', {'allPosts': allPosts, 'cat': cat, 'x': x})


