from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self, author):
        question = Question(**self.cleaned_data)
        question.author = author
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        return self.cleaned_data

    def save(self, author):
        data = self.cleaned_data
        data['question'] = Question.objects.get(pk=data['question'])
        answer = Answer(**self.cleaned_data)
        answer.author = author
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)