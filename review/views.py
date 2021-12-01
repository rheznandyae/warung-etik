from django.http import response
from django.shortcuts import render

def tulis(request):
    context = {}
    return render(request, 'tulis-review.html', context=context)
