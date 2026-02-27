

from django.http import HttpResponse
from django.shortcuts import render

from assignment.models import About
from blogs.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published")
    posts = Blog.objects.filter(is_featured=False, status="Published")
    try:
        about = About.objects.get()
    except :
        about = None

    context = {
        'about': about,
        'featured_posts':featured_posts,
        'posts':posts,
    }
    return render(request, 'home.html', context=context)