from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from.models import Room

import json

User = get_user_model()

def index(request):
    return render(request, 'chat/index.html')

@login_required
def check(request):
    try:
        r = Room.objects.get(user1=request.user) 
    except Room.DoesNotExist:
        r = None
    
    if (r is None):
        new_room = Room(
            user1=request.user,
            user2= User.objects.get(is_superuser=True)
        )
        new_room.save()
        print("Saved")
        
    r = Room.objects.get(user1=request.user)
    rn = r.name
    
    return redirect('chat:room', room_name=rn)

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
