from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('profile/<str:user_id>/', views.manage_profile, name='manage_profile'),  # Example view for managing user profile
]
