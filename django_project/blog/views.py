from django.shortcuts import render

posts = [
    {
        'author': 'RichU',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Today'
    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'Tomorrow'
    }
]

# Create your views here.


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
