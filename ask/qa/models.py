from django.db import models
from django.contrib import auth.models.User

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField(10)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(Likes)

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
		