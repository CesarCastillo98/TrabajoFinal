from django.http import HttpResponse


def hola_mundo(request):
    return HttpResponse("Hi, World")