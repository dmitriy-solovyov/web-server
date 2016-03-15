from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from qa.models import Question
from qa.models import Answer
from django.http import Http404
from forms import AnswerForm, AskForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question_list_all(request):
	questions = Question.objects.order_by('-id')
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'all_questions.html' , {
		'questions' : page.object_list,
		'paginator' : paginator, 
		'page': page,
	})

def popular_questions(request):
	questions = Question.objects.order_by('-rating')
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page)
	return render(request, 'popular_questions.html' , {
		'questions' : page.object_list,
		'paginator' : paginator, 
		'page': page,
	})

def question_with_answers(request, id):
	form = AnswerForm()
	try:
		question = Question.objects.get(id=id)
	except Question.DoesNotExist:
		raise Http404
	answers = Answer.objects.filter(question_id=id)
	return render(request, 'question.html' , {
		'question' : question,
		'answers' : answers,
	}) 

def question_add(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			url = reverse('question-with-answers', args=(question.id,))
			return HttpResponseRedirect(url)
			
	else:
		form = AskForm()
	return render(request, 'question_add.html', {
		'form' : form,
	}) 

def answer_add(request):
	 if request.method == "POST":
		 form = AnswerForm(request.POST)
		 if form.is_valid():
			 answer = form.save()
			 url = reverse('question-with-answers', args=(answer.question_id,))
			 return HttpResponseRedirect(url)
	 else:
		form = AnswerForm()
	 return HttpResponseRedirect('/')