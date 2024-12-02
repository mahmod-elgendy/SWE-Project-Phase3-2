from django.contrib import admin
from django.urls import path, include  # Import `include` for including app-specific URLs

# Import views from apps if needed
from apps.accounts import views  

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # User accounts functionality
    path('api/accounts/<str:user_id>/', views.manage_profile, name='manage_profile'),

    # Posts functionality (added this line)
    path('api/posts/', include('apps.posts.urls')),  # Includes the URLs from the `posts` app
]
