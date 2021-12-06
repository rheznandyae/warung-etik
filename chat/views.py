from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import json

def index(request):
    return render(request, 'chat/index.html')

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': request.user.username,
    })

def chat_admin(request):
    return render(request, 'chat/chat_admin.html')

def chat_pelanggan(request):
    return render(request, 'chat/chat_pelanggan.html')
