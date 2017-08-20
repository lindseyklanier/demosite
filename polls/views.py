from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'polls/test.html', {})

def test(request):
    return render(request, 'polls/test.html', {})