from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('sign_up/', views.sign_up, name='users-sign-up'),  # Url for sign up page
    path('profile/', views.profile, name='users-profile'),  # Url for Profile Page

    # Using built in Login View for login
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html') , name='users-login'),

    # Using built in Logout View for logging out, this redirects to index page directly
    path('logout/', auth_view.LogoutView.as_view(next_page='blog-index') , name='users-logout'),
]

# For saving Media of users
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)