from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def home(request):
    context = {
        'chats': Message.objects.all()
    }
    return render(request, 'chat/chat.html', context)

