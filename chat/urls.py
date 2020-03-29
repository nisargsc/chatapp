from django.urls import path
from . import views as chat_views

urlpatterns = [
    path('', chat_views.home, name='chat-home'),
]

