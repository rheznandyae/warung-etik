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
    if request.user.is_superuser:
        try:
            r = Room.objects.latest('name') 
        except Room.DoesNotExist:
            return render(request, 'chat/no_room.html')
        
        rn = r.name
        return redirect('chat:room', room_name=rn)
        
    else:
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
            r = Room.objects.get(user1=request.user)
        rn = r.name
        return redirect('chat:room', room_name=rn)
    
    

@login_required
def room(request, room_name):
    rooms = Room.objects.all()
    current_room = Room.objects.get(name=room_name)
    is_super_user = True if request.user.is_superuser else False
    context = {
        'room_name': room_name,
        'username': request.user.username,
        'rooms': rooms,
        'is_super_user': is_super_user,
        'current_room': current_room
    }
    return render(request, 'chat/room.html', context=context)

def chat_admin(request):
    return render(request, 'chat/chat_admin.html')

def chat_pelanggan(request):
    return render(request, 'chat/chat_pelanggan.html')
