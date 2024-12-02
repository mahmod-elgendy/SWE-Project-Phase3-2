from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_posts, name='manage_posts'),  # List or create posts
    path('<str:post_id>/', views.manage_posts, name='manage_post'),  # Retrieve, update, or delete a specific post
]
