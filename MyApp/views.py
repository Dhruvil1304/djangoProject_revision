from django.shortcuts import render
from django.http import HttpResponse
from . models import Feature


def index(request):
    # context = {
    #     "name": "Dhruvil",
    #     "age": 22,
    #     "nationality": "Indian"
    # }
    feature1 = Feature()
    feature1.id = 1
    feature1.name = "Fast"
    feature1.details = "Our service is very fast"

    feature2 = Feature()
    feature2.id = 1
    feature2.name = "Reliable"
    feature2.details = "Our service is very reliable"

    feature3 = Feature()
    feature3.id = 1
    feature3.name = "Easy access"
    feature3.details = "Our service is very easy to access"

    features = [feature1, feature2, feature3]
    return render(request, 'index.html', {'features': features})


def counter(request):
    text = request.POST["text"]
    words = len(text.split())
    return render(request, 'counter.html', {'words': words})
