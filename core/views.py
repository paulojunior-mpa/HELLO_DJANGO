from django.shortcuts import render, HttpResponse

# Create your views here.

def helo(request, nome, idade, sexo):
    return HttpResponse('<h1>HELLO {} de {} anos do {}<h1>'.format(nome, idade, sexo))
