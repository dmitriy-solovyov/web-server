from django import forms
from qa.models import Question
from qa.models import Answer

class AskForm(forms.Form):
	title = forms.CharField()
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		self.cleaned_data = super(AskForm, self).clean()
		return self.cleaned_data

	def save(self):
		self.cleaned_data['author_id'] = '1'
	        self.cleaned_data['rating'] = '1'
		return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
#	question = forms.IntegerField(widget=forms.HiddenInput)
	question = forms.IntegerField()

	def clean(self):
		self.cleaned_data = super(AnswerForm, self).clean()
                return self.cleaned_data

	def save(self):
		question = Question.objects.get(id=self.cleaned_data['question'])
	#	self.cleaned_data['question_id'] = question.id
		self.cleaned_data['question']= question
		self.cleaned_data['author_id'] = '1'
		return Answer.objects.create(**self.cleaned_data)



