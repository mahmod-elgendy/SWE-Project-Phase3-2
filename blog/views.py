
from django.shortcuts import render
from .models import Post
from .firebase_helper import get_data, set_data, update_data, delete_data, push_data

def firebase_posts(request):
    # Get posts data from Firebase
    firebase_data = get_data('posts')  # 'posts' is the Firebase reference
    return render(request, 'blog/firebase_posts.html', {'firebase_data': firebase_data})

def add_post_to_firebase(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        data = {
            'title': title,
            'content': content,
        }
        # Push data to Firebase
        new_post_key = push_data('posts', data)
        return render(request, 'blog/post_added.html', {'new_post_key': new_post_key})
    return render(request, 'blog/add_post.html')
def home(request):
    # Get posts from both Django and Firebase
    django_posts = Post.objects.all()
    firebase_posts = get_data('posts')  # Firebase posts stored under 'posts'

    context = {
        'posts': django_posts,
        'firebase_posts': firebase_posts,
    }

    return render(request, 'blog/home.html', context)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})