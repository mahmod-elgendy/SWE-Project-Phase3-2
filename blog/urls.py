
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('firebase-posts/', views.firebase_posts, name='firebase-posts'),
    path('add-post/', views.add_post_to_firebase, name='add-post-to-firebase'),
]

