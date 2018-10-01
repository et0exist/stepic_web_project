from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from qa.models import Question, Answer
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.views.generic import ListView
from django.template import Context, Template
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


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


def login_(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# Net proverki na dubliruushegosya polzovatelya
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def get_question(request, slug):
    question = get_object_or_404(Question, pk=slug)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(author=request.user)
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.id})
    return render(
        request,
        'question.html',
        {
            'question': question,
            'form': form
        }
    )


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save(author=request.user)
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


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


def new(request):
    return HttpResponse('New page')
