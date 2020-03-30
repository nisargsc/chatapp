from django.urls import path
from . import views as chat_views

urlpatterns = [
    path('', chat_views.chatpage, name='chat-home'),
    path('chat/', chat_views.chatpage, name='chat-home'),

]

