from django.shortcuts import render

def chat_admin(request):
    return render(request, 'chat/chat_admin.html')

def chat_pelanggan(request):
    return render(request, 'chat/chat_pelanggan.html')