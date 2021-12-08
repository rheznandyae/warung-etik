from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def chat_admin(request):
    return render(request, 'chat/chat_admin.html')

def chat_pelanggan(request):
    return render(request, 'chat/chat_pelanggan.html')