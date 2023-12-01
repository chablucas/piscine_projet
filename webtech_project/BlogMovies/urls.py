from django.urls import path, include
from BlogMovies.views_news import pageDisplay, search_view, login_view, register_view, custom_logout, post_details
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', pageDisplay, name='blog_page'),
    path('search/', search_view, name='search_view'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', custom_logout, name='logout'),
    path('post/<str:parameter_value>/', post_details, name='post_details'),
    
]
