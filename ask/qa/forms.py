from django import forms
from qa.models import Question
from qa.models import Answer

class AskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField(widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
 		super(AskForm, self).__init__(*args, **kwargs)

	def clean(self):
		tmp = 1

	def save(self):
		self.cleaned_data['author'] = '1'
		return Question.object.create(**self.cleaned_data)


class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(10)

	def __init__(self, *args, **kwargs):
 		super(AnswerForm, self).__init__(*args, **kwargs)

	def clean(self):
		tmp = 1

	def save(self):
		self.cleaned_data['author'] = '1'
		return Answer.object.create(**self.cleaned_data)


