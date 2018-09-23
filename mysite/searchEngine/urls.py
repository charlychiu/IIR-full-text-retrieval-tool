from django.urls import path

from . import views

app_name = 'searchEngine'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload'),
    path('load', views.load_file, name='load'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]