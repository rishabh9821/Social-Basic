from django.contrib import admin
from django.urls import path, include
from blogApp import views
from django.contrib.auth import views as auth_views

app_name = 'blogApp'

urlpatterns = [
    ## Post URLs
    path('', views.PostListView.as_view(), name='post-list'),
    path('myPosts/', views.MyPostListView.as_view(), name="my-post-list"),
    path('post-<post_pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('createPost/', views.PostCreateView.as_view(), name='post-create'),
    path('post-<post_pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('post-<post_pk>/update', views.PostUpdateView.as_view(), name='post-update'),

    ## Comment URLs
    path('comment-<comment_pk>/delete', views.CommentDeleteView.as_view(), name='comment-delete'),

    ## Authorization Views
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]