from django.shortcuts import render, get_object_or_404
from app.models import Post
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'app/lista_posts.html', {'posts': posts})

def detalhe_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'app/detalhe_post.html', {'post': post})

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

