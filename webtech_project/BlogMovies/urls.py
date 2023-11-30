from django.urls import path, include
from BlogMovies.views_news import pageDisplay, detailDisplay, form_comment, search_view, login_view, register_view, custom_logout
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', pageDisplay, name='blog_page'),
    path('detail/', detailDisplay, name = 'detail'),
    path('form/', form_comment, name ='form'),
    path('search/', search_view, name='search_view'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', custom_logout, name='logout'),
]
