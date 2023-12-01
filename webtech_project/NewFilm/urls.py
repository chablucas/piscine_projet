from django.urls import path
from .views import form_comment


urlpatterns = [
    path('formulaire/', form_comment, name='form')
]
