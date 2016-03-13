from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^$', views.question_list_all),
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^question/(?P<id>\d+)/', views.question_with_answers),
    url(r'^ask/', views.test),
    url(r'^popular/', views.popular_questions),
    url(r'^new/', views.test),
]