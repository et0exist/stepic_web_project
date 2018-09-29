from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from qa.models import Question, Answer
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from qa.forms import AskForm, AnswerForm
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


def login(request):
    return HttpResponse('Login page')


def signup(request):
    return HttpResponse('Signup page')


def get_question(request, slug):
    question = get_object_or_404(Question, pk=slug)
    if request.method == 'POST':
        post_parameters = request.POST.copy()
        post_parameters.setlist('question', [slug])
        form = AnswerForm(post_parameters)
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
        return render_to_response(
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
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render_to_response('ask.html', {'form': form})


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
