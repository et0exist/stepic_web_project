from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def test(request, *args, **kwargs):
#     return HttpResponse('OK')

from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def home(request, *args, **kwargs):
    return HttpResponse('Home page')


def login(request, *args, **kwargs):
    return HttpResponse('Login page')


def signup(request, *args, **kwargs):
    return HttpResponse('Signup page')


def ask(request, *args, **kwargs):
    return HttpResponse('Ask page')


def popular(request, *args, **kwargs):
    return HttpResponse('Popular page')


def new(request, *args, **kwargs):
    return HttpResponse('New page')


def question(request, *args, **kwargs):
    return HttpResponse(
        'Question {}'.format(' '.join(request.path.split('/')[2:]))
    )
