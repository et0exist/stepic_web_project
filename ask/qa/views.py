from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.http import Http404
from models import Question, Answer
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse


def home(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(
        request,
        'new.html',
        {
            'questions': page.object_list,
            'paginator': paginator,
            'page': page,
        }
    )


def login(request):
    return HttpResponse('Login page')


def signup(request):
    return HttpResponse('Signup page')


def get_question(request, slug):
    question = get_object_or_404(Question, pk=slug)
    return render(
        request,
        'question.html',
        {
            'question': question,
        }
    )


def ask(request):
    return HttpResponse('Ask page')


def popular(request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(
        request,
        'popular.html',
        {
            'questions': page.object_list,
            'paginator': paginator,
            'page': page,
        }
    )


def new(request, *args, **kwargs):
    return HttpResponse('New page')
