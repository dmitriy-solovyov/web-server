from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from qa.models import Question
from qa.models import Answer
from django.http import Http404

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question_list_all(request):
	questions = Question.objects.all()
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
	try:
		question = Question.objects.get(id=id)
	except Question.DoesNotExist:
		raise Http404
	answers = Answer.objects.get(question_id=id)
	return render(request, 'question.html' , {
		'question' : question,
		'answers' : answers,
	}) 
