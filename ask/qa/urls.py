from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^$', views.question_list_all),
    url(r'^login/', views.user_login),
    url(r'^signup/', views.signup),
    url(r'^question/(?P<id>\d+)/', views.question_with_answers, name='question-with-answers'),
    url(r'^ask/', views.question_add),
    url(r'^popular/', views.popular_questions),
    url(r'^new/', views.test),
    url(r'^answer/', views.answer_add),
]
