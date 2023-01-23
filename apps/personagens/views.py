from django.http import HttpResponse


def ola(request):
    return HttpResponse('Olá, to em personagens')

