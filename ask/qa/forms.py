from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self, author_id=1):
        question = Question(**self.cleaned_data)
        question.author = User.objects.get(pk=author_id)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        return self.cleaned_data

    def save(self, author_id=1):
        data = self.cleaned_data
        data['question'] = Question.objects.get(pk=data['question'])
        answer = Answer(**data)
        answer.author = User.objects.get(pk=author_id)
        answer.save()
        return answer
