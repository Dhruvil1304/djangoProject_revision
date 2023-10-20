from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # context = {
    #     "name": "Dhruvil",
    #     "age": 22,
    #     "nationality": "Indian"
    # }
    return render(request, 'index.html')


def counter(request):
    text = request.POST["text"]
    words = len(text.split())
    return render(request, 'counter.html', {'words': words})
