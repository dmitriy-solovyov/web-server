from django import forms
from django.forms import ModelForm
from qa.models import Question
from qa.models import Answer
from django.contrib.auth.models import User

class AskForm(ModelForm):
	class Meta:
        	model = Question
        	exclude = ['added_at','rating','author','likes']

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
#	question = forms.IntegerField(widget=forms.HiddenInput)
	question = forms.IntegerField()

	def clean(self):
		self.cleaned_data = super(AnswerForm, self).clean()
                return self.cleaned_data

	def save(self,request):
		question = Question.objects.get(id=self.cleaned_data['question'])
	#	self.cleaned_data['question_id'] = question.id
		self.cleaned_data['question']= question
		self.cleaned_data['author_id'] = request.user.id
		return Answer.objects.create(**self.cleaned_data)

class SignUpForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean(self):
		self.cleaned_data = super(SignUpForm, self).clean()
		return self.cleaned_data

	def save(self):
		return User.objects.create_user(**self.cleaned_data)

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean(self):
		self.cleaned_data = super(LoginForm, self).clean()
		return self.cleaned_data
