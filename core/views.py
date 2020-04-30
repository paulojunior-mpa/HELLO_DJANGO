from django.shortcuts import render, HttpResponse

# Create your views here.

def helo(request, nome, idade):
    return HttpResponse('<h1>HELLO {} de {} anos<h1>'.format(nome, idade))
