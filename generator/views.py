from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random


def password(request: HttpRequest) -> HttpResponse:
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    password = ''
    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})
