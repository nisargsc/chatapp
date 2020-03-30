from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import ChatInputForm


@login_required
def chatpage(request):
    if request.method == 'POST':
        form = ChatInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat-home')
    else:
        form = ChatInputForm()

    return render(request, 'chat/chat.html', {'form': form, 'chats': Message.objects.all()})
