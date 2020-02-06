from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Comment

# Create your views here.

def hockey(request):
    data = Comment.objects.all()
    context = { 
        'data': data,
    }
    if request.method == 'POST':
        comment_text = request.POST['comment']
        Comment.objects.create(comment_text=comment_text)

    return render(request, 'discuss/hockey.html', context,)


def baseball(request):
    return render(request, 'discuss/baseball.html',)

def basketball(request):
    return render(request, 'discuss/basketball.html',)

def football(request):
    return render(request, 'discuss/football.html',)