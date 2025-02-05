from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('my_posts/', views.myPosts, name='blog-my-posts'),
    # Calls functions for editing and deleting posts and viewing them in detailed view
    path('post_detial/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),
]